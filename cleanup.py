import time
import os
import shutil
from filesystem import FileSystem, Directory

class OptimizationManager:
    def __init__(self, filesystem: FileSystem):
        self.filesystem = filesystem

    def optimize(self) -> dict:
        start_time = time.time()
        old_fragmentation = self.filesystem.fragmentation_index

        # Simulate defragmentation by reorganizing files
        for _, directory in self.filesystem.get_all_directories():
            for file_name, file in list(directory.files.items()):
                if not file.is_deleted:
                    # Move file to ensure contiguous space (simplified)
                    new_path = os.path.join(directory.path, f"temp_{file_name}")
                    shutil.move(file.path, new_path)
                    shutil.move(new_path, file.path)

        # Clean up deleted files
        for _, directory in self.filesystem.get_all_directories():
            files_to_remove = [name for name, file in directory.files.items() if file.is_deleted]
            for name in files_to_remove:
                if os.path.exists(os.path.join(directory.path, name)):
                    os.remove(os.path.join(directory.path, name))
                del directory.files[name]
            directory._scan()  # Rescan to update file list

        self.filesystem.fragmentation_index = max(0, self.filesystem.fragmentation_index - 10)
        self.filesystem.free_space = shutil.disk_usage(self.filesystem.base_path).free
        optimization_time = time.time() - start_time
        return {
            "optimization_time": optimization_time,
            "old_fragmentation": old_fragmentation,
            "new_fragmentation": self.filesystem.fragmentation_index
        }

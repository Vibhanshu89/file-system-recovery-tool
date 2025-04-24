import pickle
import os
import shutil
from filesystem import FileSystem, Directory

class RecoveryManager:
    def __init__(self, filesystem: FileSystem, backup_file: str = "fs_backup.pkl"):
        self.filesystem = filesystem
        self.backup_file = backup_file

    def backup(self) -> None:
        # Backup current directory structure and files
        backup_data = {
            "root_path": self.filesystem.base_path,
            "free_space": self.filesystem.free_space,
            "fragmentation_index": self.filesystem.fragmentation_index
        }
        with open(self.backup_file, 'wb') as f:
            pickle.dump(backup_data, f)
        # Copy files to backup directory
        backup_dir = os.path.join(self.filesystem.base_path, "backup")
        if os.path.exists(backup_dir):
            shutil.rmtree(backup_dir)
        shutil.copytree(self.filesystem.base_path, backup_dir, dirs_exist_ok=True)

    def recover(self) -> bool:
        try:
            with open(self.backup_file, 'rb') as f:
                backup_data = pickle.load(f)
                # Restore from backup directory
                backup_dir = os.path.join(self.filesystem.base_path, "backup")
                if os.path.exists(backup_dir):
                    # Remove current directory content
                    for item in os.listdir(self.filesystem.base_path):
                        item_path = os.path.join(self.filesystem.base_path, item)
                        if os.path.isfile(item_path):
                            os.remove(item_path)
                        elif os.path.isdir(item_path) and item != os.path.basename(backup_dir):
                            shutil.rmtree(item_path)
                    # Copy backup content
                    for item in os.listdir(backup_dir):
                        source_path = os.path.join(backup_dir, item)
                        target_path = os.path.join(self.filesystem.base_path, item)
                        if os.path.isfile(source_path):
                            shutil.copy2(source_path, target_path)
                        else:
                            shutil.copytree(source_path, target_path, dirs_exist_ok=True)
                    # Reinitialize filesystem with restored directory
                    self.filesystem.root = Directory(os.path.basename(self.filesystem.base_path), self.filesystem.base_path)
                    self.filesystem.free_space = shutil.disk_usage(self.filesystem.base_path).free
                    self.filesystem.fragmentation_index = backup_data["fragmentation_index"]
                    self.filesystem.current_dir = self.filesystem.root
                    # Clean up backup directory
                    if os.path.exists(backup_dir):
                        shutil.rmtree(backup_dir)
                    return True
                else:
                    return False
        except (FileNotFoundError, PermissionError, OSError) as e:
            print(f"Recovery error: {e}")
            return False

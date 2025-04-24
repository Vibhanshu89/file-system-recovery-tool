from typing import List
import random
import os
from filesystem import FileSystem, Directory

class CrashSimulator:
    def __init__(self, filesystem: FileSystem):
        self.filesystem = filesystem

    def simulate_crash(self) -> List[str]:
        corruption_chance = 0.3
        corrupted_files = []
        for dir_path, directory in self.filesystem.get_all_directories():
            for file_name, file in list(directory.files.items()):
                if random.random() < corruption_chance and not file.is_deleted:
                    file_path = os.path.join(directory.path, file_name)
                    try:
                        with open(file_path, 'a', encoding='utf-8') as f:
                            f.write(" [CORRUPTED_DATA]")
                        with open(file_path, 'r', encoding='utf-8') as f:
                            file.update_content(f.read())
                        corrupted_files.append(os.path.join(dir_path, file_name) if dir_path else file_name)
                    except (PermissionError, IOError) as e:
                        print(f"Error corrupting {file_path}: {e}")
                        continue
        return corrupted_files

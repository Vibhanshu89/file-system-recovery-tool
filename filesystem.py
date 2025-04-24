import os
import shutil
from datetime import datetime
from typing import Dict, Optional, List, Tuple

class File:
    def __init__(self, name: str, path: str, size: int):
        self.name = name
        self.path = path
        self.size = size
        self.created_at = datetime.fromtimestamp(os.path.getctime(path))
        self.modified_at = datetime.fromtimestamp(os.path.getmtime(path))
        self.is_deleted = False

    def update_content(self, new_content: str) -> None:
        with open(self.path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        self.size = os.path.getsize(self.path)
        self.modified_at = datetime.fromtimestamp(os.path.getmtime(self.path))

    def mark_deleted(self) -> None:
        self.is_deleted = True
        os.remove(self.path)

class Directory:
    def __init__(self, name: str, path: str, parent: Optional['Directory'] = None):
        self.name = name
        self.path = path
        self.parent = parent
        self.files: Dict[str, File] = {}
        self.subdirs: Dict[str, 'Directory'] = {}
        self.created_at = datetime.fromtimestamp(os.path.getctime(path))
        self._scan()

    def _scan(self) -> None:
        for item in os.listdir(self.path):
            item_path = os.path.join(self.path, item)
            if os.path.isfile(item_path):
                self.files[item] = File(item, item_path, os.path.getsize(item_path))
            elif os.path.isdir(item_path):
                self.subdirs[item] = Directory(item, item_path, self)

    def add_file(self, file: File) -> bool:
        if file.name in self.files:
            return False
        self.files[file.name] = file
        return True

    def add_subdir(self, subdir: 'Directory') -> bool:
        if subdir.name in self.subdirs:
            return False
        self.subdirs[subdir.name] = subdir
        return True

    def get_file(self, name: str) -> Optional[File]:
        return self.files.get(name)

    def get_subdir(self, name: str) -> Optional['Directory']:
        return self.subdirs.get(name)

    def remove_file(self, name: str) -> bool:
        if name in self.files:
            self.files[name].mark_deleted()
            del self.files[name]
            return True
        return False

class FileSystem:
    def __init__(self, base_path: str):
        self.base_path = base_path
        self.root = Directory(os.path.basename(base_path), base_path)
        self.current_dir = self.root
        self.total_space = shutil.disk_usage(base_path).total
        self.free_space = shutil.disk_usage(base_path).free
        self.fragmentation_index = 0

    def create_file(self, name: str, content: str) -> bool:
        file_path = os.path.join(self.current_dir.path, name)
        if self.free_space < len(content) or os.path.exists(file_path):
            return False
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        file = File(name, file_path, len(content))
        if self.current_dir.add_file(file):
            self.free_space -= len(content)
            self.fragmentation_index += 1
            return True
        return False

    def delete_file(self, name: str) -> bool:
        if self.current_dir.remove_file(name):
            file = self.current_dir.get_file(name)
            if file:
                self.free_space += file.size
            return True
        return False

    def read_file(self, name: str) -> Optional[str]:
        file = self.current_dir.get_file(name)
        if file and not file.is_deleted:
            with open(file.path, 'r', encoding='utf-8') as f:
                return f.read()
        return None

    def create_directory(self, name: str) -> bool:
        new_path = os.path.join(self.current_dir.path, name)
        try:
            os.mkdir(new_path)
            new_dir = Directory(name, new_path, self.current_dir)
            return self.current_dir.add_subdir(new_dir)
        except OSError as e:
            if e.winerror == 123:  # Invalid filename syntax
                print(f"Invalid directory name syntax: {new_path}")
            return False

    def change_directory(self, path: str) -> bool:
        if path == "..":
            if self.current_dir.parent:
                self.current_dir = self.current_dir.parent
                return True
            return False
        subdir = self.current_dir.get_subdir(path)
        if subdir:
            self.current_dir = subdir
            return True
        return False

    def get_all_directories(self) -> List[Tuple[str, Directory]]:
        result = [("", self.root)]
        def traverse(directory: Directory, path: str):
            for name, subdir in directory.subdirs.items():
                new_path = f"{path}/{name}" if path else name
                result.append((new_path, subdir))
                traverse(subdir, new_path)
        traverse(self.root, "")
        return result

    def get_status(self) -> dict:
        self.free_space = shutil.disk_usage(self.base_path).free
        return {
            "free_space": self.free_space,
            "total_space": self.total_space,
            "fragmentation_index": self.fragmentation_index,
            "current_path": self.current_dir.path
        }
import os

def list_files(directory):
    """Lists all files in the given directory."""
    if os.path.exists(directory):
        return os.listdir(directory)
    else:
        return []

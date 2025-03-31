import os
import shutil

def restore_deleted_files(target_folder):
    """
    Restores deleted files from 'Deleted_Files' back to the original folder.
    """
    deleted_folder = os.path.join(target_folder, "Deleted_Files")
    recovered_files = []

    if not os.path.exists(deleted_folder):
        return []

    for file in os.listdir(deleted_folder):
        source = os.path.join(deleted_folder, file)
        destination = os.path.join(target_folder, file)

        try:
            shutil.move(source, destination)
            recovered_files.append(file)
        except Exception as e:
            print(f"⚠️ Could not restore {file}: {e}")

    return recovered_files

import os

def clean_storage(target_folder):
    """
    Deletes temporary files (.tmp) and backup files (starting with 'backup_') from the target folder.
    """
    if not os.path.exists(target_folder):
        return "❌ Directory does not exist."

    removed_files = []
    for file in os.listdir(target_folder):
        if file.endswith(".tmp") or file.startswith("backup_"):
            file_path = os.path.join(target_folder, file)
            try:
                os.remove(file_path)
                removed_files.append(file)
            except Exception as e:
                return f"⚠️ Could not remove {file}: {e}"
    
    if removed_files:
        return f"✅ Removed: {', '.join(removed_files)}"
    return "ℹ️ No unnecessary files found."

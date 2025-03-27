import os

def optimize_storage():
    """Removes unnecessary files to free up space."""
    unnecessary_files = ["temp.txt", "backup_old.log"]
    removed_files = []

    for file in unnecessary_files:
        if os.path.exists(file):
            os.remove(file)
            removed_files.append(file)

    if removed_files:
        print("🗑️ Optimized storage by deleting:")
        for file in removed_files:
            print(f"   🚫 {file}")
    else:
        print("✅ No unnecessary files found.")

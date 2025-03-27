import os

def recover_files(directory):
    """Scans a directory and lists recoverable files."""
    if not os.path.exists(directory):
        print(f"❌ The directory '{directory}' does not exist.")
        return

    print(f"🔍 Scanning directory: {directory}")
    recovered_files = []

    for file in os.listdir(directory):
        if file.startswith("deleted_"):  # Simulating deleted files
            old_path = os.path.join(directory, file)
            new_path = os.path.join(directory, file.replace("deleted_", ""))
            os.rename(old_path, new_path)
            recovered_files.append(new_path)

    if recovered_files:
        print("✅ Recovered files:")
        for file in recovered_files:
            print(f"   📄 {file}")
        log_recovery(recovered_files)
    else:
        print("❌ No deleted files found.")

def log_recovery(files):
    """Logs recovered files into a text file."""
    with open("recovery_log.txt", "a") as log:
        log.write("\nRecovered Files:\n")
        for file in files:
            log.write(file + "\n")

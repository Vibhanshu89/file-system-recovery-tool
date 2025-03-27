from recovery import recover_files
from optimize import optimize_storage

def main():
    print("📂 File System Recovery Tool")
    print("1️⃣ Recover Deleted Files")
    print("2️⃣ Optimize Storage")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        directory = input("Enter the directory to scan for deleted files: ")
        recover_files(directory)
    elif choice == '2':
        optimize_storage()
    else:
        print("❌ Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()

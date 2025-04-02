# 🛠️ File System Recovery Tool

A comprehensive utility for file recovery, storage cleanup, and data loss simulation. This tool helps users manage their file systems effectively with three key functionalities.

![App Screenshot](screenshot.png) *<!-- Consider adding an actual screenshot later -->*

## ✨ Features

1. **File Restoration**  
   - Recovers deleted files from a special "Deleted_Files" directory
   - Preserves original file names and structure

2. **Storage Cleanup**  
   - Automatically removes temporary (.tmp) files
   - Cleans up backup files (prefixed with 'backup_')
   - Frees up valuable disk space

3. **Data Loss Simulation**  
   - Safe environment to test recovery procedures
   - Moves files to "Deleted_Files" without permanent deletion
   - Perfect for disaster recovery drills

## 🛠️ Installation

1. Clone the repository:
   git clone https://github.com/yourusername/file-recovery-tool.git


2. Install dependencies:
pip install -r requirements.txt


🚀 Usage
Run the application with:

streamlit run app.py
Interface Guide:
Restore Lost Files: Enter a folder path to recover deleted files

Clean Up Storage: Specify directory to remove temporary files

Simulate Data Loss: Test recovery workflow by simulating file deletion


⚠️ Important Notes
Always back up important files before using cleanup features

Simulation moves files but doesn't permanently delete them

Requires Python 3.8+ and Streamlit

📜 License
MIT License - See LICENSE for details

🤝 Contributing
Pull requests welcome! Please:

Fork the repository

Create your feature branch

Commit your changes

Push to the branch

Open a pull request

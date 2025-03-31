🛠️ File System Recovery Tool
📌 Overview
The File System Recovery Tool is designed to help users restore deleted files, clean up unused data, and simulate data loss for testing recovery techniques. Whether you accidentally delete important files or need to optimize disk space, this tool provides an efficient and user-friendly solution.

🚀 Features
1️⃣ Restore Lost Files
Retrieves files that were mistakenly deleted and placed in the Deleted_Files folder.

Moves the recovered files back to their original location.

Ensures no important data is permanently lost.

2️⃣ Clean Up Unused Data
Identifies and removes unnecessary files to free up disk space.

Deletes:

Temporary files (.tmp)

Backup files (files starting with backup_)

Helps keep storage organized and optimized.

3️⃣ Simulate Data Loss
Moves all files from a selected directory into a Deleted_Files folder.

Useful for testing recovery processes and understanding data loss scenarios.

Helps in creating a real-world data loss simulation for educational or practical purposes.

🛠️ Installation
Prerequisites
Before running the tool, ensure you have:

Python 3.10 or later installed on your system.

Streamlit, which powers the user interface.

Steps to Install
Clone the repository using Git:

bash
Copy
Edit
git clone https://github.com/Vibhanshu89/file-system-recovery-tool.git
cd file-system-recovery-tool
Install required dependencies using pip:

bash
Copy
Edit
pip install -r requirements.txt
Run the application:

bash
Copy
Edit
streamlit run app.py
📂 Project Structure
The project consists of the following files:

perl
Copy
Edit
file-system-recovery-tool/
│── app.py                 # Main Streamlit application
│── restore.py             # Handles file recovery
│── cleanup.py             # Manages storage cleanup
│── crash_sim.py           # Simulates data loss
│── requirements.txt       # Lists necessary dependencies
└── README.md              # Documentation for the project
▶️ How to Use
Launch the Application:
Run the Streamlit app using:

bash
Copy
Edit
streamlit run app.py
Follow the On-Screen Instructions:

Select a folder for file restoration, and the tool will recover lost files.

Choose a directory to clean up, and unnecessary files will be removed.

Use the simulate data loss feature to move files to Deleted_Files, allowing you to test recovery procedures.

💡 Future Enhancements
To make this tool even more powerful, planned improvements include:

File Versioning: Keep track of different versions of files to allow better restoration options.

Secure Deletion: Implement a method for permanently deleting files, making them unrecoverable.

Storage Visualization: Add a graphical representation of disk space usage for better insights.

🤝 Contributing
Contributions are always welcome! If you have ideas for improving this tool, feel free to:

Fork the repository

Make changes and create a pull request

Discuss new feature ideas in the issues section
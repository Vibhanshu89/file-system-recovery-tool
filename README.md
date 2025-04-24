File System Recovery and Optimization Tool
Overview
This project is a Python-based tool for managing, recovering, and optimizing a real-time file system. It interacts with the actual file system of your computer using Streamlit for a user interface and modular functionality for file operations, directory management, recovery, crash simulation, and optimization.
Features

File Operations: Create, read, and delete files on the real file system.
Directory Operations: Create directories and navigate the real file system.
Recovery: Backup and restore the real file system from simulated crashes.
Crash Simulation: Simulate disk crashes by corrupting real files.
Optimization: Defragment and clean up the real file system.

Installation

Clone the repository or download the files.
Install the required dependencies:pip install -r requirements.txt


Run the Streamlit app:streamlit run app.py



Usage

Enter a valid base directory path (or use the default current directory) when starting the app.
Access the tool in your browser (typically at http://localhost:8501).
Use the sidebar to navigate directories and view system status.
Explore the tabs for different operations (File Operations, Directory Operations, Recovery, Optimization).
Note: This tool modifies the real file system; use with caution and backup important data.

Modules

app.py: Main application with Streamlit UI and core file system logic.
cleanup.py: Optimization and cleanup functionality.
crash_sim.py: Crash simulation logic.
restore.py: Recovery and backup operations.
requirements.txt: Lists required Python packages.


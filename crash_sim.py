import os
import shutil
import streamlit as st

def trigger_disk_failure(target_folder):
    """
    Simulates a data loss event by moving all files to 'Deleted_Files' inside the target folder.
    """
    deleted_folder = os.path.join(target_folder, "Deleted_Files")

    # Create 'Deleted_Files' folder if it doesn't exist
    if not os.path.exists(deleted_folder):
        os.makedirs(deleted_folder)

    # Move files to Deleted_Files
    for file in os.listdir(target_folder):
        file_path = os.path.join(target_folder, file)
        if os.path.isfile(file_path):  # Ensure it's a file
            shutil.move(file_path, os.path.join(deleted_folder, file))
    
    st.success(f"✅ Simulated Data Loss! All files moved to: {deleted_folder}")

import streamlit as st
import threading
import os
import time
from restore import restore_deleted_files
from cleanup import clean_storage
from crash_sim import trigger_disk_failure

st.title("🛠️ File System Recovery Tool")

# --------------------- Step 1: Restore Lost Files ---------------------
st.header("1️⃣ Restore Lost Files")
restore_path = st.text_input("Enter folder path to restore files:")
if st.button("Restore Files"):
    if restore_path and os.path.exists(restore_path):
        result = restore_deleted_files(restore_path)
        st.success(f"✅ Recovery process completed! {result}")
    else:
        st.error("⚠️ Please enter a valid folder path!")

# --------------------- Step 2: Clean Up Storage ---------------------
st.header("2️⃣ Clean Up Unused Data")
cleanup_path = st.text_input("Enter folder path to clean (delete .tmp or backup_ files):")
if st.button("Clean Storage"):
    if cleanup_path and os.path.exists(cleanup_path):
        removed_files = clean_storage(cleanup_path)
        if removed_files:
            st.success(f"✅ Removed: {', '.join(removed_files)}")
        else:
            st.info("No unnecessary files found!")
    else:
        st.error("⚠️ Please enter a valid folder path!")



# --------------------- Step 4: Simulate Data Loss ---------------------
st.header("3️⃣ Simulate Data Loss")
loss_path = st.text_input("Enter folder path for data loss simulation:")
if st.button("Simulate Data Loss"):
    if loss_path and os.path.exists(loss_path):
        result = trigger_disk_failure(loss_path)
        st.warning(result)
    else:
        st.error("⚠️ Please enter a valid folder path!")

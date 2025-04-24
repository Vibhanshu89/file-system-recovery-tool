import streamlit as st
import os
from filesystem import FileSystem, Directory, File
from cleanup import OptimizationManager
from crash_sim import CrashSimulator
from restore import RecoveryManager

def main():
    st.set_page_config(page_title="Real-Time File System Tool", layout="wide")
    
    # Ensure base path input is always shown
    st.title("Real-Time File System Recovery & Optimization Tool")
    base_path = st.text_input("Enter Base Directory Path", value=os.getcwd(), key="base_path_input")
    
    if not base_path or not os.path.isdir(base_path):
        st.error("Invalid directory path. Using current directory or please enter a valid path.")
        base_path = os.getcwd()
    
    if 'fs' not in st.session_state or st.session_state.fs.base_path != base_path:
        st.session_state.fs = FileSystem(base_path)
        st.session_state.recovery = RecoveryManager(st.session_state.fs)
        st.session_state.crash_sim = CrashSimulator(st.session_state.fs)
        st.session_state.optimizer = OptimizationManager(st.session_state.fs)
        st.success(f"Set base path to: {base_path}")

    fs = st.session_state.fs
    recovery = st.session_state.recovery
    crash_sim = st.session_state.crash_sim
    optimizer = st.session_state.optimizer

    with st.sidebar:
        st.header("System Status")
        status = fs.get_status()
        st.write(f"Current Path: {status['current_path']}")
        st.write(f"Free Space: {status['free_space']} bytes")
        st.write(f"Total Space: {status['total_space']} bytes")
        st.write(f"Fragmentation Index: {status['fragmentation_index']}")

        st.header("Navigation")
        new_dir = st.text_input("Change Directory")
        if st.button("Change Directory"):
            if new_dir:
                if fs.change_directory(new_dir):
                    st.success(f"Changed to {new_dir}")
                else:
                    st.error(f"Directory {new_dir} not found")

    tab1, tab2, tab3, tab4 = st.tabs(["File Operations", "Directory Operations", "Recovery", "Optimization"])

    with tab1:
        st.header("File Operations")
        col1, col2, col3 = st.columns(3)
        with col1:
            file_name = st.text_input("File Name", key="create_file_name")
            file_content = st.text_area("File Content", key="file_content")
            if st.button("Create File"):
                if file_name and file_content:
                    if fs.create_file(file_name, file_content):
                        recovery.backup()
                        st.success(f"File {file_name} created")
                    else:
                        st.error("Failed to create file")
        with col2:
            read_file_name = st.text_input("File Name to Read", key="read_file_name")
            if st.button("Read File"):
                if read_file_name:
                    content = fs.read_file(read_file_name)
                    if content:
                        st.text_area("File Content", content, height=200)
                    else:
                        st.error(f"File {read_file_name} not found or deleted")
        with col3:
            delete_file_name = st.text_input("File Name to Delete", key="delete_file_name")
            if st.button("Delete File"):
                if delete_file_name:
                    if fs.delete_file(delete_file_name):
                        recovery.backup()
                        st.success(f"File {delete_file_name} deleted")
                    else:
                        st.error(f"File {delete_file_name} not found")

    with tab2:
        st.header("Directory Operations")
        col1, col2 = st.columns(2)
        with col1:
            dir_name = st.text_input("Directory Name", key="create_dir_name")
            # Validate that dir_name is not a full path
            if dir_name and ("\\" in dir_name or "/" in dir_name):
                st.error("Please enter only the directory name, not a full path.")
            elif st.button("Create Directory"):
                if dir_name:
                    if fs.create_directory(dir_name):
                        recovery.backup()
                        st.success(f"Directory {dir_name} created")
                    else:
                        st.error(f"Directory {dir_name} already exists or creation failed")
        with col2:
            if st.button("List Contents"):
                contents = f"Files: {list(fs.current_dir.files.keys())}\nDirectories: {list(fs.current_dir.subdirs.keys())}"
                st.text_area("Directory Contents", contents, height=150)

    with tab3:
        st.header("Recovery Operations")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Simulate Crash"):
                corrupted_files = crash_sim.simulate_crash()
                if corrupted_files:
                    st.warning(f"Corrupted files: {', '.join(corrupted_files)}")
                else:
                    st.info("No files corrupted")
        with col2:
            if st.button("Recover"):
                if recovery.recover():
                    st.success("System recovered from backup")
                else:
                    st.error("No backup found")

    with tab4:
        st.header("Optimization")
        if st.button("Optimize System"):
            result = optimizer.optimize()
            recovery.backup()
            st.success(f"Optimization completed in {result['optimization_time']:.6f} seconds")
            st.write(f"Fragmentation reduced from {result['old_fragmentation']} to {result['new_fragmentation']}")

if __name__ == "__main__":
    main()

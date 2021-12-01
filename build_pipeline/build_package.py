import glob
import os
import subprocess
import constants
import pipeline_helper

def has_build_directory() -> bool:
    return os.path.exists(constants.build_directory())

def prune_all_files_from_build_directory() -> None:
    if has_build_directory():
        all_build_files = glob.glob(f"{constants.build_directory()}/*")
        for file in all_build_files:            
            os.remove(file)

def build_package() -> None:
    subprocess.call("python3 -m build".split())

if __name__ == "__main__":
    pipeline_helper.set_project_base_path_as_working_directory()
    prune_all_files_from_build_directory() # Remove previous builds since the twine deployment tool can't handle multiple builds.
    build_package()

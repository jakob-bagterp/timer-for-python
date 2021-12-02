import glob
import os
import subprocess
from helper.constants import build_destination
from helper import working_directory

def has_build_directory() -> bool:
    return os.path.exists(f"./{build_destination()}")

def prune_all_files_from_build_directory() -> None:
    if has_build_directory():
        all_build_files = glob.glob(f"./{build_destination()}/*")
        for file in all_build_files:            
            os.remove(file)

def build_package() -> None:
    subprocess.call("python3 -m build".split())

if __name__ == "__main__":
    working_directory.set_as_project_base_path()
    prune_all_files_from_build_directory() # Remove previous builds since the twine deployment tool can't handle multiple builds.
    build_package()

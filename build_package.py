import glob
import os
import subprocess

_build_directory = "./dist"

def has_build_directory() -> bool:
    return os.path.exists(_build_directory)

def prune_all_files_from_build_directory() -> None:
    if has_build_directory():
        files = glob.glob(f"{_build_directory}/*")
        for file in files:            
            os.remove(file)

def build_package() -> None:
    subprocess.call(["python3", "-m", "build"])

if __name__ == "__main__":
    prune_all_files_from_build_directory() # Remove previous builds since the twine deployment tool can't handle multiple builds.
    build_package()

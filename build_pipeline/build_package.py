import subprocess
from helper import build_directory
from helper import working_directory

def build_package() -> None:
    subprocess.call("python3 -m build".split())

if __name__ == "__main__":
    working_directory.set_as_project_base_path()
    build_directory.prune_old_files() # Remove previous builds since the twine deployment tool can't handle multiple builds.
    build_package()

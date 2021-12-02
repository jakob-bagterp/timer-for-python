import glob
import os
from . import working_directory
from .constants import build_destination

def exists() -> bool:
    working_directory.set_as_project_base_path()
    return os.path.exists(f"./{build_destination()}")

def prune_old_files() -> None:
    working_directory.set_as_project_base_path()
    if exists():
        all_build_files = glob.glob(f"./{build_destination()}/*")
        for file in all_build_files:            
            os.remove(file)

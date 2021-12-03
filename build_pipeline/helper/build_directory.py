import glob
import os
from . import working_directory
from .config import destination

def exists() -> bool:
    working_directory.set_as_project_base_path()
    return os.path.exists(f"./{destination()}")

def prune_old_files() -> None:
    working_directory.set_as_project_base_path()
    if exists():
        all_build_files = glob.glob(f"./{destination()}/*")
        for file in all_build_files:            
            os.remove(file)

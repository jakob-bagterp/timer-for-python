import glob
import os
from .constants import build_destination

def exists() -> bool:
    return os.path.exists(f"./{build_destination()}")

def prune_old_files() -> None:
    if exists():
        all_build_files = glob.glob(f"./{build_destination()}/*")
        for file in all_build_files:            
            os.remove(file)

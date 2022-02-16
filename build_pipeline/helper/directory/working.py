import os
from pathlib import Path
from config import directory

def set_as_project_base_path() -> None:
    path_of_this_file = Path(__file__)
    project_base_directory = path_of_this_file.parent.parent.parent.parent.absolute() # The parent directory of the "build_pipeline" directory.
    os.chdir(project_base_directory)

def set_as_homebrew_core() -> None:
    os.chdir(directory.homebrew_core())

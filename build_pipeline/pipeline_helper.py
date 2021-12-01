import os
from pathlib import Path

def set_working_directory(directory: str) -> None:
    os.chdir(directory)

def set_project_base_path_as_working_directory() -> None:
    path_of_this_file = Path(__file__)
    project_base_directory = path_of_this_file.parent.parent.absolute() # The parent directory of this "build_pipeline".
    set_working_directory(project_base_directory)

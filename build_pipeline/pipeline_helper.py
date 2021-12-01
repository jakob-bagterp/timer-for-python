import os
import re

def set_working_directory(directory: str) -> None:
    os.chdir(directory)

def set_project_base_path_as_working_directory() -> None:
    path_of_this_file, _ = os.path.split(os.path.abspath(__file__))
    project_base_directory = re.sub(r"/build_pipeline\/?$", "", path_of_this_file, flags = re.IGNORECASE) # Assume this is the directory name of the pipeline build files.
    set_working_directory(project_base_directory)

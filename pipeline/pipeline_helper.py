import os
import re

def set_project_base_path_as_working_directory():
    path_of_this_file, _ = os.path.split(os.path.abspath(__file__))
    project_base_directory = re.sub(r"/pipeline\/?$", "", path_of_this_file, flags = re.IGNORECASE) # Assume this is the directory name of the pipeline build files.
    os.chdir(project_base_directory)

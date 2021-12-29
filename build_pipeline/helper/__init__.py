__all__ = ["deploy_package", "directory", "build_package", "run_tests"]

import subprocess
from distutils.util import strtobool
from timer.version import __version__
from config import package_name
from config.directory import temp_builds
from . import directory 

def get_version() -> str:
    return __version__

def get_release_file_name() -> str:
    return f"{package_name()}-{get_version()}.tar.gz"

def output_release_file_checksum() -> None:
    directory.working.set_as_project_base_path()
    release_file_name = get_release_file_name()
    print(f"Checksum SHA256 for {release_file_name}:")
    subprocess.call(f"shasum -a 256 ./{temp_builds()}/{release_file_name}".split())
    print("")

def prompt_user_yes_or_no(question: str) -> bool:
    """Prompt a yes/no question to the user."""

    while True:
        user_input = input(f"{question} (y/n): ")
        try:
            return bool(strtobool(user_input))
        except ValueError:
            print("Please use y/n or yes/no.\n")    

def confirm_to_proceed(question: str) -> None:
    is_confirmed = prompt_user_yes_or_no(question)
    if is_confirmed is not True:
        print("Exiting...")
        exit(0)

def execute_command_and_print(command: str) -> None:
    print(f"Executing command \"{command}\"...")
    subprocess.call(command.split())

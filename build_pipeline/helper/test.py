import subprocess
import sys
import working_directory

def run_pytest() -> None:
    working_directory.set_as_project_base_path()
    returncode = subprocess.run("pytest".split()).returncode
    sys.exit(returncode)

if __name__ == "__main__":
    run_pytest()

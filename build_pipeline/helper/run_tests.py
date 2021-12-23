import subprocess
import sys
from . import directory

def run_pytest() -> None:
    directory.working.set_as_project_base_path()
    returncode = subprocess.run("pytest".split()).returncode
    sys.exit(returncode)

if __name__ == "__main__":
    run_pytest()

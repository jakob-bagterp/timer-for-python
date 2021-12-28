import subprocess
from shutil import copyfile
from pathlib import Path
from config import directory, package_install_name
from helper import confirm_to_proceed

def homebrew_update() -> None:
    command = "brew update"
    print(f"Executing command \"{command}\"...")
    subprocess.call(command.split())

def homebrew_upgrade() -> None:
    command = "brew upgrade"
    print(f"Executing command \"{command}\"...")
    subprocess.call(command.split())

def homebrew_audit_package() -> None:
    subprocess.call(f"brew audit --strict --online {package_install_name()}".split())
 
def copy_formula_to_homebrew_formulas() -> None:
    path_of_this_file = Path(__file__)
    path_of_this_directory = path_of_this_file.parent.absolute()
    source = f"{path_of_this_directory}/formula.rb"
    destination = f"{directory.homebrew_formulas()}/{package_install_name()}.rb"
    copyfile(source, destination)

if __name__ == "__main__":
    homebrew_update()
    homebrew_upgrade()
    homebrew_audit_package()
    confirm_to_proceed()
    copy_formula_to_homebrew_formulas()

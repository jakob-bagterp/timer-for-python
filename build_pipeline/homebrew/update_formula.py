from shutil import copyfile
from pathlib import Path
from config import directory, package_install_name
from helper import confirm_to_proceed, execute_command_and_print

def homebrew_update() -> None:
    execute_command_and_print("brew update")

def homebrew_upgrade() -> None:
    execute_command_and_print("brew upgrade")

def homebrew_audit_package() -> None:
    execute_command_and_print(f"brew audit --strict --online {package_install_name()}")
 
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
    confirm_to_proceed() # If any errors or extraordinary manual updates are needed.
    copy_formula_to_homebrew_formulas()

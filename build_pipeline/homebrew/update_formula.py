from shutil import copyfile
from pathlib import Path
from config import directory, package_install_name
from helper import confirm_to_proceed, execute_command_and_print
from helper.directory import working as working_directory

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

def homebrew_git_checkout_branch(branch: str) -> None:
    working_directory.set_as_homebrew_core()
    execute_command_and_print(f"git checkout {branch}")

def homebrew_git_check_status() -> None:
    working_directory.set_as_homebrew_core()
    execute_command_and_print("git status")

def homebrew_git_stage_file(filename: str) -> None:
    working_directory.set_as_homebrew_core()
    execute_command_and_print(f"git add {filename}")

if __name__ == "__main__":
    homebrew_git_checkout_branch("master")
    homebrew_update()
    homebrew_update() # Sometimes Homebrew isn't fully updated after one round so we do it a second time.
    homebrew_upgrade()
    homebrew_audit_package()
    confirm_to_proceed("Continue?") # If any errors or extraordinary manual updates are needed.
    copy_formula_to_homebrew_formulas()
    homebrew_git_stage_file(f"Formula/{package_install_name()}.rb")
    homebrew_git_check_status()
    confirm_to_proceed("Commit changes and create pull request?")

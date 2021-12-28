from shutil import copyfile
from pathlib import Path
from config import directory, package_install_name

def copy_formula_to_homebrew_formulas() -> None:
    path_of_this_file = Path(__file__)
    path_of_this_directory = path_of_this_file.parent.absolute()
    source = f"{path_of_this_directory}/formula.rb"
    destination = f"{directory.homebrew_formulas()}/{package_install_name()}.rb"
    copyfile(source, destination)

if __name__ == "__main__":
    copy_formula_to_homebrew_formulas()

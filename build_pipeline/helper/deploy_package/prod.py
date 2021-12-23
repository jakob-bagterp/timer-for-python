import subprocess
from shutil import copyfile
from .. import directory
from .. import get_release_file_name
from config.directory import releases, temp_builds

def copy_package_to_releases() -> None:
    directory.working.set_as_project_base_path()
    release_file_name = get_release_file_name()
    source = f"./{temp_builds()}/{release_file_name}"
    destination = f"./{releases()}/{release_file_name}"
    copyfile(source, destination)

def deploy_to_pypi() -> None:
    directory.working.set_as_project_base_path()
    subprocess.call(f"twine upload {temp_builds()}/*".split())

if __name__ == "__main__":
    copy_package_to_releases()
    deploy_to_pypi()

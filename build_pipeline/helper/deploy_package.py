import subprocess
from . import working_directory
from config.directory import temp_builds

def deploy_to_pypi() -> None:
    working_directory.set_as_project_base_path()
    subprocess.call(f"twine upload {temp_builds()}/*".split())

if __name__ == "__main__":
    deploy_to_pypi()

import subprocess
from helper.config import destination
from helper import working_directory

def deploy_to_pypi() -> None:
    working_directory.set_as_project_base_path()
    subprocess.call(f"twine upload {destination()}/*".split())

if __name__ == "__main__":
    deploy_to_pypi()

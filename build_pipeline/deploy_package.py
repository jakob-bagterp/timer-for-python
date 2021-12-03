import subprocess
from helper.config import destination
from helper import working_directory

def deploy_package() -> None:
    subprocess.call(f"twine upload {destination()}/*".split())

if __name__ == "__main__":
    working_directory.set_as_project_base_path()
    deploy_package()

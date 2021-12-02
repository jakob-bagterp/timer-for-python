import subprocess
from helper.constants import build_destination
from helper import working_directory

def deploy_test_package() -> None:
    subprocess.call(f"python3 -m twine upload --repository testpypi {build_destination()}/*".split())

if __name__ == "__main__":
    working_directory.set_as_project_base_path()
    deploy_test_package()

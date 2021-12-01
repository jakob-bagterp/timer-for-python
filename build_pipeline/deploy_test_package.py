import subprocess
import constants
import pipeline_helper

def deploy_test_package() -> None:
    subprocess.call(f"python3 -m twine upload --repository testpypi {constants.build_directory()}/*".split())

if __name__ == "__main__":
    pipeline_helper.set_project_base_path_as_working_directory()
    deploy_test_package()

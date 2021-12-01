import subprocess
from pipeline_constants import build_directory
import pipeline_helper

def deploy_package() -> None:
    subprocess.call(f"twine upload {build_directory()}/*".split())

if __name__ == "__main__":
    pipeline_helper.set_project_base_path_as_working_directory()
    deploy_package()

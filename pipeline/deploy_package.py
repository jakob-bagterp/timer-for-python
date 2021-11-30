import subprocess
import pipeline_helper

def deploy_package() -> None:
    subprocess.call("twine upload dist/*".split()) # Destination directory "dist" viewed from the project base.

if __name__ == "__main__":
    pipeline_helper.set_project_base_path_as_working_directory()
    deploy_package()

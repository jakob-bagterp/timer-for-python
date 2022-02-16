import subprocess
from .. import directory, output_release_file_checksum
from config.directory import temp_builds

def deploy_to_pypi() -> None:
    directory.working.set_as_project_base_path()
    subprocess.call(f"twine upload {temp_builds()}/*".split())

if __name__ == "__main__":
    output_release_file_checksum()
    deploy_to_pypi()

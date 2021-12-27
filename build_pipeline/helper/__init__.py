__all__ = ["deploy_package", "directory", "build_package", "run_tests"]

import subprocess
from timer.version import __version__
from config import package_name
from config.directory import temp_builds
from . import directory 

def get_version() -> str:
    return __version__

def get_release_file_name() -> str:
    return f"{package_name()}-{get_version()}.tar.gz"

def output_release_file_checksum() -> None:
    directory.working.set_as_project_base_path()
    release_file_name = get_release_file_name()
    print(f"Checksum SHA256 for {release_file_name}:")
    subprocess.call(f"shasum -a 256 ./{temp_builds()}/{release_file_name}".split())
    print("")

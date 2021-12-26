__all__ = ["deploy_package", "directory", "build_package", "run_tests"]

import subprocess

def get_version() -> str:
    from timer.version import __version__
    return __version__

def get_release_file_name() -> str:
    from config import package_name
    return f"{package_name()}-{get_version()}.tar.gz"

def output_release_file_checksum() -> None:
    from config.directory import releases
    from . import directory 
    directory.working.set_as_project_base_path()
    release_file_name = get_release_file_name()
    print(f"Checksum SHA256 for {release_file_name}:")
    subprocess.call(f"shasum -a 256 ./{releases()}/{release_file_name}".split())
    print("")

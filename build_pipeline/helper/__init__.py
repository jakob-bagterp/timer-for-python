__all__ = ["deploy_package", "directory", "build_package", "run_tests"]

def get_version() -> str:
    from timer.version import __version__
    return __version__

def get_release_file_name() -> str:
    from config import package_name
    return f"{package_name()}-{get_version()}.tar.gz"

import subprocess

from . import directory


def build_package() -> None:
    directory.working.set_as_project_base_path()
    subprocess.call("python3 -m build".split())


if __name__ == "__main__":
    # Remove previous builds since the twine deployment tool can't handle multiple builds.
    directory.build.prune_old_files()
    build_package()

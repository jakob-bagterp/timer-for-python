import glob
import os

from config.directory import temp_builds

from .. import directory


def exists() -> bool:
    directory.working.set_as_project_base_path()
    return os.path.exists(f"./{temp_builds()}")


def prune_old_files() -> None:
    directory.working.set_as_project_base_path()
    if exists():
        all_build_files = glob.glob(f"./{temp_builds()}/*")
        for file in all_build_files:
            os.remove(file)

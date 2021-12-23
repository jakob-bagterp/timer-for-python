def temp_builds() -> str:
    """Destination directory "dist" viewed from the project base. Usage examples: f"./{constants.build_directory()}" as directory ("./dist") or f"{constants.build_directory()/*}" as glob ("dist/*")."""

    return "dist"

def releases() -> str:
    return "releases"

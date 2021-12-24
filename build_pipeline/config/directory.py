def temp_builds() -> str:
    """Destination directory "dist" viewed from the project base. Usage examples: f"./{config.temp_builds()}" as directory ("./dist") or f"{config.temp_builds()/*}" as glob ("dist/*")."""

    return "dist"

def releases() -> str:
    """Directory of different final version of release packages, e.g. to be distributed via Homebrew."""
    
    return "releases"

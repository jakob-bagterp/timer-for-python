def temp_builds() -> str:
    """Destination directory "dist" viewed from the project base. Usage examples: f"./{config.temp_builds()}" as directory ("./dist") or f"{config.temp_builds()/*}" as glob ("dist/*")."""

    return "dist"

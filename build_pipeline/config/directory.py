def temp_builds() -> str:
    """Destination directory "dist" viewed from the project base. Usage examples: f"./{config.temp_builds()}" as directory ("./dist") or f"{config.temp_builds()/*}" as glob ("dist/*")."""

    return "dist"


def homebrew_core() -> str:
    """Path of Homebrew core library."""

    return "/usr/local/Homebrew/Library/Taps/homebrew/homebrew-core"


def homebrew_formulas() -> str:
    """Path of Homebrew formulas of the core library."""

    return f"{homebrew_core()}/Formula"

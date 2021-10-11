import subprocess

def deploy_package() -> None:
    subprocess.call(["twine", "upload", "dist/*"])

if __name__ == "__main__":
    deploy_package()

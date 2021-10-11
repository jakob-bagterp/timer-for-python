import subprocess

def deploy_test_package() -> None:
    subprocess.call(["python3", "-m", "twine", "upload", "--repository", "testpypi", "dist/*"])

if __name__ == "__main__":
    deploy_test_package()

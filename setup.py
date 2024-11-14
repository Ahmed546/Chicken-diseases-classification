import setuptools

with open("Readme.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__="0.0.0"

REPO_NAME="Chiken-Disease-classification"
AUTHOR_USER_NAME="waleed"
SRC_REPO="ChickenDiseaseClassifier"
AUTHOR_EMAIL="AHMEDWALEED003@GMAIL.COM"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for chiken disease classifier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/Ahmed546/Chicken-diseases-classification",
    project_urls={
        "Bug Tracker": f"https://github.com/Ahmed546/Chicken-diseases-classification/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")

)
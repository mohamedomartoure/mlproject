from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ." # Ignore the current package {-e . means editable install of the package in the current directory}
def get_requirements(file_path: str) -> List[str]:
    """ This function will return the list of requirements """
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements] # Remove newline characters

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

# Metadata and dependencies for the ML project
setup(
    name="ml_project",
    version="0.0.1",
    author="Beno",
    author_email="mohamedtoure.secure@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
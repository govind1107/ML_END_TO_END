from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str)->List[str]:
    """
    this function will return the list of requirements
    """

    requirement = []

    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace("\n","") for req in requirement]

        if HYPHEN_E_DOT in requirement:
            requirement.remove(HYPHEN_E_DOT)

    return requirement





setup(
    name = 'ML_END_TO_END',
    version = '0.0.1',
    author='Govind Lipne',
    author_email= 'govind.lipne11@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')

)
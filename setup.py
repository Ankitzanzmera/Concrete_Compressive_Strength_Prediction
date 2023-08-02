from setuptools import setup,find_packages
from typing import List

hyphen_e_dot = '-e .' # if you wtire -e . in requirement the at time of installing setup.py will be triggered and all package will install again.

def get_requirements(file_path:str) -> List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

        return requirements

setup(
    name='Concrete_Compressive_Strength_prediction',
    version='0.0.1',
    author='Ankit_Zanzmera',
    author_email='22msrds052@jainuniversity.ac.in',
    install_requires = get_requirements('requirement.txt'),
    packages=find_packages()
)
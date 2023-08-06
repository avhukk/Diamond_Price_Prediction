from setuptools import find_packages, setup
from typing import List 

HYPHEN_E_DOT = '-e .'

## Automatically import all the requirements from requirements.txt
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open (file_path) as file_obj: 
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements
        

setup(
    name = 'RegressionProject',
    version= '0.0.1',
    author= 'Abhishek Vivek Hukkerikar',
    author_email= 'avhukkerikar@gmail.com', 
    install_requires = get_requirements('requirements.txt'), 
    packages=find_packages()
)
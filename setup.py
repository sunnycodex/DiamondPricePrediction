from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT='-e .'
# function for install_requires from requirements.txt
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

        return requirements
    
    
setup(
    name='DiamondPricePrediction',
    author='Sunny',
    author_email='sa2182780@gmail.com',
    version='0.0.1',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)
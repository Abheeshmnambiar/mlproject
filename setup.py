from setuptools import find_packages,setup
from typing import List


def get_requirements(filepath:str)->List[str]:
    '''
    this function will return list of requirements/ packages 
    '''
    requirements =[]
    with open("requirements.txt") as file_obj:
        requirements =file_obj.readlines()
        requirements =[req.replace("\n","") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name="mlproject",
    version ="0.0.1",
    author="Abheesh",
    author_email="abheeshmnambiar@gmail.com",
    packages=find_packages(),
    #install_requires =["pandas","numpy","seaborn"]
    install_requires = get_requirements("requirements.txt")

)
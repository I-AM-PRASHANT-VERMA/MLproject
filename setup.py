from setuptools import find_packages, setup  
from typing import List  

HYPEN_E_DOT = "-e ."  

def get_requirements(file_path: str) -> List[str]:  
    """  
    This function returns the list of requirements. 

    """
    requirements = []  
    with open(file_path) as file_obj:  
        requirements = file_obj.readlines()
        #the lines in requirement.txt will have /n  along with name so we have to remvoe that  
        requirements = [req.replace("\n", "") for req in requirements]
        # list comprehention to replace \n
        # we dont want to have the -e . in the requirement it can give the error  
        if HYPEN_E_DOT in requirements:  
            requirements.remove(HYPEN_E_DOT)  
    return requirements  

setup(  
    name='MLproject',  
    version='0.0.1',  
    author='Prashant Verma',  
    author_email='Prashantverma813@gmail.com',  
    packages=find_packages(),  
    install_requires=get_requirements('requirements.txt')  
)  

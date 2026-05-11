from setuptools import find_packages, setup # type: ignore
from typing import List

def get_requirements(file_path:str)-> List[str]:
    '''
    this function return the list of Requirements
    
    '''
    Requirements = []
    
    with open(file_path) as file_obj:
        Requirements = file_obj.readlines()
        Requirements = [Req.replace("\n","") for Req in Requirements]
        return Requirements



setup(
    name= "MLProjectPipeline",
    version="1.0",
    author="Ekendra Yadav",
    author_email="ekendrayadav632@gmail.com",
    packages= find_packages(),
    install_requires=get_requirements("Requirements.txt")
)
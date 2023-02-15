from setuptools import find_packages,setup
# from typing import List 

# def get_requirements()->List[str]:
#     """
#     This function returns list of requirements
#     """
#     # requirement_list:List[str]=[]
#     with open('requirements.txt', 'r') as f:
#         requirement_list = [line.strip() for line in f]

#     return requirement_list

setup(
    name="sensor", 
    version="0.0.1", 
    author="Satish",
    author_email="satishk.singh@outlook.com",
    packages = find_packages(),
    install_requires =["pymango==4.2.0"]#get_requirements(),

)


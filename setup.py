from setuptools import find_packages, setup
from typing import List

#new changes

def get_requirements()-> List[str]:
  """This function will return the list of requirements"""
  requirements_list : List[str] = []



  return requirements_list
  
setup(
  name="sensor",
  version="0.0.1",
  author="Arnav Adarsh",
  author_email="arnavadarsh26@gmail.com",
  packages=find_packages(),
  intall_requires=get_requirements()
)
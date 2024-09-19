from setuptools import find_packages,setup
from typing import List

#define the -e .
TRIGGER_SETUP_FILE= '-e .'
def getRequiredPackages(file_path:str)->List[str]:
   '''
      this function for getting the required installed libraries from requiremnt.txt file
   '''
   packges_install=[]
   with open(file_path) as file:
      packges_install=file.readlines() 
      packges_install=[r.replace('\n',"") for r in packges_install]
      if TRIGGER_SETUP_FILE in packges_install:
         packges_install.remove(TRIGGER_SETUP_FILE)
   return packges_install
      
      


setup (

   name="end_to_end_ML",
   version='1.0.0',
   author_email='ayah.elghaysh.12345@gmail.com',
   author='Aya Elsawy',
   packages=find_packages(),
   install_require=getRequiredPackages('requirements.txt')
)
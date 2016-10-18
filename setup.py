#from distutils.core import setup
from setuptools import setup
#https://docs.python.org/2/distutils/setupscript.html

setup(name="LNTk",
      version='0.1',
      author="Vincent Antaki",
      author_email="vincent.antaki@mail.mcgill.ca",
      url="",
#      packages=["networkx",'python-community','images2gif']
      install_requires=["networkx",'selenium','xvfbwrapper','Pillow']
      )

#optionnal_packages = ['nose','sphinx','coverage.py']
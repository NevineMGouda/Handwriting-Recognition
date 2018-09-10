# Go to terminal, cd to this file's path and "sudo python setup.py install"
from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()
setup(
   name='HR-ML',
   version='1.0',
   description='Handwritting Recognition Module',
   author='Team 28: Ahmed Dawood, Mona Mohamed Elamin & Nevine Gouda',
   long_description=long_description,
   packages=['scripts'],  #same as name
   install_requires=['numpy', 'scipy', 'Pillow','scikit-learn'], #external packages as dependencies #pip install psutil

)
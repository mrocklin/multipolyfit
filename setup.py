from os.path import exists
from setuptools import setup

setup(name='multipolyfit',
      version='0.0.1',
      description='Multivariate Polynomial fitting with NumPy',
      url='http://github.com/mrocklin/multipolyfit',
      author='Matthew Rocklin',
      author_email='mrocklin@gmail.com',
      license='BSD',
      packages=['multipolyfit'],
      long_description=open('README.md').read() if exists("README.md") else "",
      zip_safe=False)

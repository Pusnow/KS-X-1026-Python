#!/usr/bin/env python

from setuptools import setup, find_packages
from codecs import open
from os import path
import ksx1026

here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='ksx1026',
      version=ksx1026.__version__,
      description='Python Implementation of KS X 1026 ',
      author='Wonsup Yoon',
      author_email='pusnow@yonsei.ac.kr',
      url='https://github.com/Pusnow/KS-X-1026-Python',
      packages=find_packages(),
      license='MIT',
      long_description=long_description,
      keywords='hangul unicode',
      )

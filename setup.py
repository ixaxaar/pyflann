#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='flann',

    version='1.6.13',
    description='flann is the python 3.6 bindings for FLANN - Fast Library for Approximate Nearest Neighbors.',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/pypa/flann',

    # Author details
    author='Marius Muja & Gefu Tang, Maintainer: Russi Chatterjee',
    author_email='root@ixaxaar.in',

    # Choose your license
    license='BSD',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='Approximate Nearest Neighbors',

    packages=find_packages(),
    package_dir={'pyflann.lib': 'pyflann/lib'},
    package_data={'pyflann.lib': [
        'darwin/*.dylib', 'win32/x86/*.dll', 'win32/x64/*.dll', 'linux/*.so']},

    install_requires=['numpy'],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    python_requires='>=3',
)


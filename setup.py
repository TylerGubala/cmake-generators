#! /usr/bin/python
# -*- coding: future_fstrings -*-
"""
Query cmake-generators
"""

from setuptools import find_packages, setup

setup(name='cmake-generators',
      version='1.0.1',
      packages=find_packages(),
      description='Query cmake-generators',
      long_description=open("./README.md", 'r').read(),
      long_description_content_type="text/markdown",
      keywords="cmake, Automation",
      classifiers=["Development Status :: 3 - Alpha",
                   "Environment :: Win32 (MS Windows)",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: "
                   "GNU General Public License v3 (GPLv3)",
                   "Natural Language :: English",
                   "Programming Language :: Python :: 3.4",
                   "Programming Language :: Python :: 3.5",
                   "Programming Language :: Python :: 3.6",
                   "Programming Language :: Python :: 3.7",
                   "Programming Language :: Python :: Implementation :: CPython"],
      author='Tyler Gubala',
      author_email='gubalatyler@gmail.com',
      license='GPL-3.0',
      python_requires=">=3.4.0",
      url="https://github.com/TylerGubala/cmake-generators"
    )

#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = "PyV8",
    version = "1.0-r549",
    author = "Jan Alonzo",
    author_email = "",
    description = "", 
    long_description = "",
    license = "",
    url = "https://github.com/jmalonzo/pyv8-linux-x64",
    packages=find_packages(),
    zip_safe = False,
    package_data = {
        'pyv8': ['*.so'],     # include .so files when installed with pip/git
    },
    classifiers = [
        "Development Status :: 1.0-r549",
        "Environment :: Server",
        "Intended Audience :: Developers",
        "Operating System :: Linux",
        "Programming Language :: Python",
        ]
)

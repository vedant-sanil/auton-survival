
# File: setup.py 
# Author(s): 
# Created: Wed Mar 20 11:49:20 EST 2022 
# Description:
# Acknowledgements:
# Copyright (c) 2022 Carnegie Mellon University
# This code is subject to the license terms contained in the code repo.

import io
import os
import sys
import shutil
import setuptools
import subprocess
from glob import glob
from distutils.command.build_py import build_py
from distutils.util import convert_path

with io.open('README.md', 'r', encoding="utf-8") as fp:
    description = fp.read()

with open('requirements.txt', 'r') as reqfile:
    req = [line.strip() for line in reqfile if line and not line.startswith('#')]

pkgs = [elem.replace('auton_survival/', '') for elem in list(glob('auton_survival/datasets/*', recursive=True))+list(glob('auton_survival/models/**', recursive=True)) if os.path.isfile(elem)] 

def Main():
    main_ns = {}
    ver_path = convert_path('auton_survival/_version.py')
    with open(ver_path) as ver_file:
        exec(ver_file.read(), main_ns)

    VERSION = main_ns['__version__']
    NAME = 'auton_survival'
    #VERSION = __VERSION__
    VERSION = '0.0.1'

    setuptools.setup(
        name=NAME,
        version=VERSION,
        install_requires=req,
        description=r"Auton Survival - an open source package for Regression, Counterfactual Estimation, Evaluation and Phenotyping with Censored Time-to-Events",
        long_description=description,
        package_data={NAME:pkgs},
        packages=setuptools.find_packages(),
        python_requires=">=3.6",
        include_package_data=True,
        author='Chirag Nagpal',
        maintainer='Chirag Nagpal',
        maintainer_email='chiragn@andrew.cmu.edu',
        keywords=['auton-survival', 'survival analysis', 'regression'],
        license='Apache-2.0',
        long_description_content_type='text/markdown',
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'License :: OSI Approved :: Apache Software License',
            'Topic :: Scientific/Engineering']
    )

if __name__=="__main__":
    Main()
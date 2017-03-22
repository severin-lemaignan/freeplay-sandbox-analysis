#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['freeplay_sandbox_analysis', 'freeplay_sandbox_analysis.plugins'],
    package_dir={'': 'src'},
    scripts=['scripts/analysis']
)

setup(**d)

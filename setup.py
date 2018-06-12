#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import re
import os
import ast
from setuptools import setup


_version_re = re.compile(r'__version__\s+=\s+(.*)')


with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

if os.path.isdir("click") and not os.path.exists("trio_click"):
    os.symlink("click","trio_click")

with io.open('click/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

setup(
    name='trio-click',
    author='Matthias Urlichs',
    author_email='matthias@urlichs.de',
# I don't really want to replace Armin as the author here,
# but uploading to pypi kindof requires it.
#   author='Armin Ronacher',
#   author_email='armin.ronacher@active-4.com',
    version=version,
    url='http://github.com/python-trio/trio-click',
    packages=['trio_click'],
    #maintainer='Pallets team',
    #maintainer_email='contact@palletsprojects.com',
    long_description=readme,
    description='A simple trio-compatible wrapper around optparse for '
                'powerful command line utilities.',
    license='BSD',
    extras_require={
        'dev': [
            'pytest>=3',
            'coverage',
            'tox',
            'sphinx',
        ],
        'docs': [
            'sphinx',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    build_requires=[
        'pytest-trio',
    ],
    install_requires=[
        'trio>=0.3',
    ],
    python_requires=">=3.5",
)

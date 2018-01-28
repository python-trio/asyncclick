import re
import ast
import os
from setuptools import setup


_version_re = re.compile(r'__version__\s+=\s+(.*)')


with open('click/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

if os.path.isdir("click") and not os.path.exists("trio_click"):
    os.symlink("click","trio_click")

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
    description='A simple trio-compatible wrapper around optparse for '
                'powerful command line utilities.',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    build_requires=[
        'pytest-trio',
    ],
    install_requires=[
        'trio>=0.3',
    ],
)

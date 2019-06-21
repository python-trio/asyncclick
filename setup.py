import io
import re
import os
import ast
from setuptools import setup

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

if os.path.isdir("click") and not os.path.exists("asyncclick"):
    os.symlink("click","asyncclick")

with io.open("click/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = \'(.*?)\'", f.read()).group(1)

setup(
    name='asyncclick',
    author='Matthias Urlichs',
    author_email='matthias@urlichs.de',
# I don't really want to replace Armin as the author here,
# but uploading to pypi kindof requires it.
#   author='Armin Ronacher',
#   author_email='armin.ronacher@active-4.com',
    version=version,
    url='http://github.com/python-trio/asyncclick',
    packages=['asyncclick'],
    #maintainer='Pallets team',
    #maintainer_email='contact@palletsprojects.com',
    long_description=readme,
    description='A simple anyio-compatible fork of Click, for '
                'powerful command line utilities.',
    license='BSD',
    tests_require=[
        'pytest',
        'pytest-trio',
    ],
    extras_require={
        'dev': [
            'pytest>=3',
            'pytest-trio',
            'pytest-runner',
            'coverage',
            'tox',
            'sphinx',
        ],
        'docs': [
            'sphinx',
        ],
        ':python_version < "3.7"': [
            'async_exit_stack',
        ],
    },
    project_urls={
        "Code": "https://github.com/python-trio/asyncclick",
        "Issue tracker": "https://github.com/python-trio/asyncclick/issues",
    },
    include_package_data=True,
    python_requires=">=3.6",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=[
        'anyio',
    ],
)

from setuptools import setup

setup(
    name="asyncclick",
    install_requires=[
        "colorama; platform_system == 'Windows'",
        "importlib-metadata; python_version < '3.8'",
    ],
)

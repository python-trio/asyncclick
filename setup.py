from setuptools import setup

setup(
    name="asyncclick",
    use_scm_version={"version_scheme": "guess-next-dev", "local_scheme": "dirty-tag"},
    setup_requires=["setuptools_scm"],
    install_requires=[
        "colorama; platform_system == 'Windows'",
        "importlib-metadata; python_version < '3.8'",
    ],
)

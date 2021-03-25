from setuptools import setup

setup(name="click", install_requires=["colorama; platform_system == 'Windows'"],
	use_scm_version={"version_scheme": "guess-next-dev", "local_scheme": "dirty-tag"})

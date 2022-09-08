from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in aperture/__init__.py
from aperture import __version__ as version

setup(
	name="aperture",
	version=version,
	description="Aperture",
	author="Aperture",
	author_email="aperture@yopmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

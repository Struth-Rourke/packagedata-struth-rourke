# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="newpackage-struth-rourke", # the name that you will install via pip
    version="1.3",
    author="Rourke Struthers",
    author_email="struthers.rourke@gmail.com",
    description="New custom pandas package",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/Struth-Rourke/packagedata-struth-rourke",
    #keywords="",
    packages=find_packages() # ["newpandaspackage"]
)


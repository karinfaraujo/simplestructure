from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="simplestructure",
    version="0.0.1",
    author="karinf",
    author_email="karinf.araujo@gmail.com",
    description="Create a package using the simple structure of a module.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/karinfaraujo/simplestructure",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
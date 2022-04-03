from setuptools import setup

NAME = "setuptools-pep621-readme"

# Would actually retrieve this dynamically from package version.py
__version__ = "0.1.dev1"

# Would actually carry out a dynamic substition of selected content
# from the project README.md
readme = "This is a test readme."

setup(
    version=__version__,
    long_description=readme,
    long_description_content_type="text/markdown",
    # readme=readme,
)

# coding: utf-8

from setuptools import setup, find_packages

NAME = "rengars_marketplace"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Rengars Marketplace API",
    author_email="",
    url="",
    keywords=["Swagger", "Rengars Marketplace API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['rengars_marketplace=rengars_marketplace.__main__:main']},
    long_description="""\
    An API for headhunters and job applicants. Headhunters post job offers for which an applicant can post an application.
    """
)

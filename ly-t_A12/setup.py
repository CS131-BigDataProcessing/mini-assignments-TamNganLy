from setuptools import setup, find_packages

setup(
    name='crime_test',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    description='A package for validating and analyzing crime data',
    author='Tam Ly',
    author_email='tamly@email.com',
)

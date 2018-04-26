""" Setup """
from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

'''
with open('LICENSE') as f:
    license = f.read()
'''

setup(
    name='MySocialNetwork',
    version='0.0.1',
    description='simple development of a social network for study',
    long_description=README,
    author='Matheus Sbaraglini',
    author_email='matheus.sbaraglini@hotmail.com',
    url='https://github.com/MatheusSbaraglini',
    # license=license,
    packages=find_packages()
)
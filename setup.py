from setuptools import setup

setup(
    name='gwyfile',
    version='0.1',
    description='Pythonic implementation of the Gwyddion file format',
    author='Tino Wagner',
    author_email='ich@tinowagner.com',
    package_dir = {'': '.'},
    packages = ['gwyfile'],
)

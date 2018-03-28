from setuptools import setup, find_packages
from codecs import open
from os import path


# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='game',
    version='0.0.1',
    description='Game II UI prototype',
    long_description=long_description,
    url='https://github.com/ad1v7/GameII',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License'
    ],
    include_package_data=True,
    install_requires=[
        'PyQt5>=5.10.1'
    ],
    entry_points={
        'console_scripts': ['game=game.main:main']
    }
)

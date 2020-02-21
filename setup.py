from setuptools import setup

setup(
    name='boxrec-scrapper',
    version=1.0,
    packages=['boxrec'],
    install_requires=['pytest'],
    entry_points={'console_scripts': ['boxrec-scrapper = boxrec.cli.main:main']}
)
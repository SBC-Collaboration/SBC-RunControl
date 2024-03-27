from setuptools import find_packages, setup

setup(
    name='sbcbinaryformat',
    packages=find_packages(include=['sbcbinaryformat']),
    version='0.1.3',
    description='SBC Binary Format library',
    author='Hector Hawley Herrera',
    install_requires=['numpy']
)

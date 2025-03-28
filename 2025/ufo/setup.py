from setuptools import setup, find_packages

setup(
    name="ufo_area",
    version="0.1.0",
    author="Pawel",
    description="Biblioteka do obliczania powierzchni UFO",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.26"
    ],
)
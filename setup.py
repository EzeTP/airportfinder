from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="airportfinder",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Python library for airport lookup by IATA code or name",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/airportfinder",
    packages=find_packages(),
    package_data={
    'pyalgo2': ['data/airports.json']
    },  
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=[
        "requests",
    ],
    python_requires=">=3.7",
)

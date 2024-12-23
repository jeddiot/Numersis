from setuptools import setup, find_packages

setup(
    name="numersis",  # Package name
    version="0.1.0",  # Initial version
    author="Jedd",
    author_email="yangjedd@gmail.com",
    description="A Python package for numerical analysis",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jeddiot/Numersis",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        # List dependencies here
        "numpy",
        "scipy"
    ],
)
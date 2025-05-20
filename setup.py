from setuptools import setup, find_packages

setup(
    name="quantum_simulator",
    version="0.1",
    packages=find_packages(),
    requires=[
        "numpy",
    ],
    author="Brandon Fong",
    description="A minimal quantum simulator using NumPy.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/bfong-08/quantum-circuit-simulator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)

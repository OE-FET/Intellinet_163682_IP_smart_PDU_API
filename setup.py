# -*- coding: utf-8 -*-

# system imports
from setuptools import setup, find_packages  # type: ignore


setup(
    name="intellinet_pdu",
    version="0.1.0",
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages("src"),
    package_dir={"": "src"},
    setup_requires=["wheel"],
    install_requires=[
        "lxml",
        "bs4",
    ],
    zip_safe=False,
    python_requires=">=3.6",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
)

"""
Setup configuration for DevTimeTracker.

This file allows installing the package and provides
the 'devtime' command-line utility.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="devtime-tracker",
    version="0.1.0",
    author="CynicznyKot",
    author_email="iotajot@gmail.com",
    description="Smart time tracker for developers. Automatically tracks time in IDEs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cynicznykot/DevTimeTracker",
    project_urls={
        "Bug Tracker": "https://github.com/cynicznykot/DevTimeTracker/issues",
        "Documentation": "https://github.com/cynicznykot/DevTimeTreacker/blob/master/README.md",
        "Source Code": "https://github.com/cynicznykot/DevTimeTracker",
    },
    packages=find_packages(include=["src", "src.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operation System :: OS Independent",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Productivity",
        "Topic :: Utilities",
    ],
    entry_points={
        "console_scripts": [
            "devtime=src.cli.main:main",
        ],
    },
    install_requires=requirements,
    python_requires=">=3.10",
    keywords="time tracker, productivity, developers, ide, pycharm, vscode",
)
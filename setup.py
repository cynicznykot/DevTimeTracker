"""
Setup configuration for DevTimeTracker.

This file allows installing the package and provides
the 'devtime' command-line utility.
"""

from setuptools import setup, find_packages

setup(
    name="devtime-tracker",
    version="0.1.0",
    description="Smart time tracker for developers",
    author="CynicznyKot",
    url="https://github.com/cynicznykot/DevTimeTracker",
    packages=find_packages(include=["src", "src.*"]),
    entry_points={
        "console_scripts": [
            "devtime=src.cli.main:main",
        ],
    },
    install_requires=[
        "pygetwindow>=0.0.9; sys_platform == 'win32'",
    ],
    python_requires=">=3.8",
)
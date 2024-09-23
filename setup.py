from setuptools import setup, find_packages
from pathlib import Path  # Import Path from pathlib

setup(
    name="Actual_Leads_Reporter",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "leads=src.main:main",
        ],
    },
    install_requires=[
        "click>=8.1.7,<9.0.0",  # Add Click as a project dependency with a version range
    ],
    extras_require={
        "dev": [
            "black",
            "setuptools",
        ],
    },
    python_requires=">=3.6",
    long_description=(
        Path(__file__).parent / "README.md"
    ).read_text(),  # Add the long description directly
    long_description_content_type="text/markdown",  # Specify the content type of the long description
)

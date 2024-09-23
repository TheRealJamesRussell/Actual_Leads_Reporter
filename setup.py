from setuptools import setup, find_packages
from pathlib import Path  # Import Path from pathlib

setup(
    name="Actual_Leads_Reporter",
    version="0.2.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "leads=main:main",
        ],
    },
    install_requires=[
        "click",  # Add Click as a project dependency
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

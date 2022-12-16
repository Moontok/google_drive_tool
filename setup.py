from setuptools import setup, find_packages

setup(
    name='google_sheets_tool',
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "googleapi"
    ]
)
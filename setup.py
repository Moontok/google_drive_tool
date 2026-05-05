from setuptools import setup, find_packages

setup(
    name='google_drive_tool',
    version="1.0.1",
    packages=find_packages(),
    install_requires=[
        "googleapi"
    ]
)
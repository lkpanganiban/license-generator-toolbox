from setuptools import setup, find_packages


setup(
    name="license-toolbox",
    version="0.1",
    description="Generates a license key and file.",
    author="Ian Panganiban",
    author_email="lkp@noypimaps.com",
    packages=find_packages(),
    entry_points={"console_scripts": ["license-generator=license_toolbox.run:main"]},
    install_requires=[
        "fire"
    ],
)

from setuptools import setup, find_packages

setup(
    name="CurrConv",  # The name of your package
    version="1.0.0",  # Version number
    description="Currency Converter using Current Stocks",  # Brief description
    long_description=open('README.md').read(),  # Detailed description (usually from README)
    long_description_content_type="text/markdown",  # Specifies the type of the long description
    author="William B",  # Your name (or your organization's name)
    author_email="willdev2025@outlook.com",  # Your email
    url="https://github.com/Wdboyes13/currencyconverter",  # Project URL
    packages=find_packages(),  # Automatically find all packages in your project
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
    "Operating System :: OS Independent",
    ],
    install_requires=[  # External dependencies your project needs
        "yfinance",  # Example dependency
    ],
    python_requires=">=3.10",  # Specify which versions of Python your project is compatible with
)

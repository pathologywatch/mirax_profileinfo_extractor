from setuptools import setup, find_packages

setup(
    name="mirax_profileinfo_extractor",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # List your dependencies here
    ],
    author="GODARD Tuatini",
    author_email="tuatini@pathologywatch.com",
    description="A simple library that extracts profile information from a MIRAX file.",
    license="MIT",
    keywords="mirax profile extractor",
    url="https://github.com/pathologywatch/mirax_profileinfo_extractor",
    classifiers=[
        "Development Status :: 2 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "License :: OSI Approved :: MIT License",
    ],
)
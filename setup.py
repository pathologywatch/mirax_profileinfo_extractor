from setuptools import setup, find_packages, Extension

ext = Extension(
    name='profileinfo_extractor',
    sources=['src/lib/profileinfo_extractor.c'],
)

setup_args = dict(
    packages=find_packages(where="src"),  # list
    package_dir={"": "src"},
    ext_modules=[ext],
)

setup(**setup_args)

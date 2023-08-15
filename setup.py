import sys
from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext


class CustomBuildExt(build_ext):
    def get_ext_filename(self, ext_name):
        if sys.platform == "darwin":
            return ext_name + ".dylib"
        return super().get_ext_filename(ext_name)


ext = Extension(
    name='libprofileinfo_extractor',
    sources=['lib/profileinfo_extractor.c'],
)

setup_args = dict(
    packages=find_packages(where="src"),
    cmdclass=dict(build_ext=CustomBuildExt),
    package_dir={"": "src"},
    ext_modules=[ext],
)

setup(**setup_args)

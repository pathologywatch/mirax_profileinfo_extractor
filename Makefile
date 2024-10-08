# Detect the OS
UNAME := $(shell uname)
ifeq ($(UNAME), Darwin)
    # MacOS
    LIBEXT=.dylib
else
    # assume Linux
    LIBEXT=.so
endif
TARGET=libprofileinfo_extractor$(LIBEXT)
CC=gcc

all: create_wheels

create_wheels:
	python -m pip install --upgrade build
	python -m build

build_conda:
	conda build ./conda_pkg --output-folder ./dist/

upload_conda:
	rm -rf ./dist/
	conda build ./conda_pkg --output-folder ./dist/
	anaconda upload ./dist/*/*.tar.bz2

test_pypi_upload:
    python -m pip install --upgrade twine cibuildwheel
    python -m cibuildwheel --output-dir wheelhouse
    python -m twine upload --repository testpypi wheelhouse/*

# Use __token__ as username and the Pypi API token as password
pypi_upload:
    python -m pip install --upgrade twine cibuildwheel
    python -m cibuildwheel --output-dir wheelhouse
    python -m twine upload wheelhouse/*

shared_lib: lib/profileinfo_extractor.c
	mkdir -p dist
	$(CC) $< -shared -fPIC -o dist/$(TARGET)

clean:
	rm -fR libprofileinfo_extractor.so \
	libprofileinfo_extractor.dll \
	libprofileinfo_extractor.dylib \
	build \
	dist \
	wheelhouse \
	src/mirax_profileinfo_extractor.egg-info

run-python:
	python3 extractor.py

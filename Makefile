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

shared_lib: lib/profileinfo_extractor.c
	mkdir -p dist
	$(CC) $< -shared -fPIC -o dist/$(TARGET)

clean:
	rm -fR libprofileinfo_extractor.so \
	libprofileinfo_extractor.dll \
	libprofileinfo_extractor.dylib \
	build \
	dist \
	src/mirax_profileinfo_extractor.egg-info

run-python:
	python3 extractor.py

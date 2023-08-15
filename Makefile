CC=gcc
CFLAGS=-shared -fPIC

all: create_wheels

create_wheels:
	python -m pip install --upgrade build
	python -m build

libprofileinfo_extractor.so: src/mirax_profileinfo_extractor
	$(CC) $(CFLAGS) profileinfo_extractor.c -o libprofileinfo_extractor.so

clean:
	rm -fR libprofileinfo_extractor.so build dist src/mirax_profileinfo_extractor.egg-info

run-python:
	python3 extractor.py

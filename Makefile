CC=gcc
CFLAGS=-shared -fPIC

all: create_wheels

create_wheels:
	python setup.py bdist_wheel

libprofileinfo_extractor.so: profileinfo_extractor.c
	$(CC) $(CFLAGS) profileinfo_extractor.c -o libprofileinfo_extractor.so

clean:
	rm -f libprofileinfo_extractor.so build dist

run-python:
	python3 extractor.py

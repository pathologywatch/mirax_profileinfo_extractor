CC=gcc
CFLAGS=-shared -fPIC

all: libprofileinfo_extractor.so

libprofileinfo_extractor.so: profileinfo_extractor.c
	$(CC) $(CFLAGS) profileinfo_extractor.c -o libprofileinfo_extractor.so

clean:
	rm -f libprofileinfo_extractor.so

run-python:
	python3 extractor.py

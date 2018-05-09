# Copyright 2018 NLCI (http://www.nlci.in/fonts/)
# Apache License v2.0

SHELL   = /bin/sh

charsets=nlci-deva.py nlci-knda.py nlci-taml.py nlci-all.py nrsi-all.py google-all.py

all:
	install -m 644 $(charsets) "$(HOME)/builds/pyfontaine/pyfontaine/fontaine/charsets/internals"

clean:
	rm -f *~

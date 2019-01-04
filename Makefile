# Copyright 2018-2019 NLCI (http://www.nlci.in/fonts/)
# Apache License v2.0

SHELL   = /bin/sh

charsets=nlci-deva.py nlci-knda.py nlci-taml.py nlci-all.py nrsi-all.py google-all.py

all:
	install -m 600 $(charsets) "$(HOME)/builds/pyfontaine/fontaine/charsets/internals"
	install -m 600 $(charsets) "$(HOME)/builds/pyfontaine3/fontaine/charsets/internals"

clean:
	rm -f *~

# Copyright 2017-2020 NLCI (http://www.nlci.in/fonts/)
# Apache License v2.0

SHELL   = /bin/sh

charsets=nlci-deva.py nlci-deva-ext.py nlci-knda.py nlci-taml.py nlci-indic-num.py nlci-vedic.py nlci-all.py nrsi-all.py nrsi-rtl.py google-all.py

all:
	install -m 600 $(charsets) "$(HOME)/builds/pyfontaine/fontaine/charsets/internals"

clean:
	rm -f *~

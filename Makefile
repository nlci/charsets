SHELL   = /bin/sh

charsets=nlci-deva.py nlci-taml.py nrsi-all.py

all:
	install -m 644 $(charsets) "$(HOME)/builds/pyfontaine/pyfontaine/fontaine/charsets/internals"

clean:
	rm -f *~

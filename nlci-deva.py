# -*- coding: utf8 -*-

# Copyright 2018-2019 NLCI (http://www.nlci.in/fonts/)
# Apache License v2.0

class Charset:
    common_name = 'NLCI: Devanagari script'
    native_name = 'Devanagari script'
    abbreviation = 'Deva'
    key = 0x0915
    glyphs = \
        [0x0310] + \
        list(xrange(0x0900, 0x097F+1))

# -*- coding: utf8 -*-

# Copyright 2018-2019 NLCI (http://www.nlci.in/fonts/)
# Apache License v2.0

class Charset:
    common_name = 'NLCI: Devanagari script extended'
    native_name = 'Extended Devanagari script'
    abbreviation = 'DevaExt'
    key = 0x0915
    glyphs = \
        list(xrange(0x1CD0, 0x1CF9+1)) + \
        list(xrange(0xA830, 0xA839+1)) + \
        list(xrange(0xA8E0, 0xA8FF+1))

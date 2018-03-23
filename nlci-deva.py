# -*- coding: utf8 -*-


class Charset:
    common_name = 'NLCI: Devanagari script'
    native_name = 'Devanagari script'
    abbreviation = 'Deva'
    key = 0x0915
    glyphs = \
        [0x0310] + \
        list(xrange(0x0900, 0x097F+1)) + \
        list(xrange(0x1CD0, 0x1CF9+1)) + \
        list(xrange(0xA8E0, 0xA8FD+1))

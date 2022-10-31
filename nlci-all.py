# -*- coding: utf8 -*-

# Copyright 2018-2022 NLCI (http://www.nlci.in/fonts/)
# Apache License v2.0

class Charset:
    common_name = 'NLCI-All fonts'
    native_name = 'Characters for all Indic fonts'
    abbreviation = 'Indic'
    key = 0x0965
    glyphs = [
        # Latin
        0x20A8,  # RUPEE SIGN

        # Indic
        0x20B9,  # INDIAN RUPEE SIGN
        0x0964,  # DEVANAGARI DANDA
        0x0965,  # DEVANAGARI DOUBLE DANDA
        0x0951,  # DEVANAGARI STRESS SIGN UDATTA
        0x0952,  # DEVANAGARI STRESS SIGN ANUDATTA

        # Quotations and text marking
        0x2308,  # LEFT CEILING
        0x2309,  # RIGHT CEILING
        0x230A,  # LEFT FLOOR - request from Dan
        0x230B,  # RIGHT FLOOR - request from Dan
        0x231C,  # TOP LEFT CORNER
        0x231D,  # TOP RIGHT CORNER
        0x231E,  # BOTTOM LEFT CORNER - used by Steve
        0x231F,  # BOTTOM RIGHT CORNER - used by Steve
        0x2E22,  # TOP LEFT HALF BRACKET - now in Charis
        0x2E23,  # TOP RIGHT HALF BRACKET - now in Charis
        0x2E24,  # BOTTOM LEFT HALF BRACKET - request from Steve - now in Charis
        0x2E25,  # BOTTOM RIGHT HALF BRACKET - request from Steve - now in Charis

        # Footnote callers
        # 0x2756,  # BLACK DIAMOND MINUS WHITE X - suggested by Dan - not in Charis

        # MacRoman not in Codepage 1252
        0x03A9,  # GREEK CAPITAL LETTER OMEGA

        # Variation Selectors
        # list(xrange(0xE0100, 0xE01EF)) # VARIATION SELECTOR-17..VARIATION SELECTOR-256 - non BMP characters not handled

        # Superscripted footnote callers
        0x2070,  # SUPERSCRIPT ZERO
        0x207B,  # SUPERSCRIPT MINUS
        0x207D,  # SUPERSCRIPT LEFT PARENTHESIS
        0x207E,  # SUPERSCRIPT RIGHT PARENTHESIS
        0x2074,  # SUPERSCRIPT FOUR
        0x2075,  # SUPERSCRIPT FIVE
        0x2076,  # SUPERSCRIPT SIX
        0x2077,  # SUPERSCRIPT SEVEN
        0x2078,  # SUPERSCRIPT EIGHT
        0x2079,  # SUPERSCRIPT NINE
    ]

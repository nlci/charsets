# -*- coding: utf8 -*-

# Copyright 2018 NLCI (http://www.nlci.in/fonts/)
# Apache License v2.0

class Charset:
    common_name = 'NLCI-All fonts'
    native_name = 'Characters for all Indic fonts'
    abbreviation = 'Indic'
    key = 0x00E9
    glyphs = [
        # Indic
        0x20A8,  # RUPEE SIGN
        0x20B9,  # INDIAN RUPEE SIGN
        0x0964,  # DEVANAGARI DANDA
        0x0965,  # DEVANAGARI DOUBLE DANDA
        # 0x0971,  # DEVANAGARI SIGN HIGH SPACING DOT
        0x0951,  # DEVANAGARI STRESS SIGN UDATTA
        0x0952,  # DEVANAGARI STRESS SIGN ANUDATTA
        0x0953,  # DEVANAGARI GRAVE ACCENT
        0x0954,  # DEVANAGARI ACUTE ACCENT
        0x1CDA,  # VEDIC TONE DOUBLE SVARITA
        0x1CDC,  # VEDIC TONE KATHAKA ANUDATTA
        0x1CDD,  # VEDIC TONE DOT BELOW
        0x1CDE,  # VEDIC TONE TWO DOTS BELOW
        0x1CDF,  # VEDIC TONE THREE DOTS BELOW
        0x1CF5,  # VEDIC SIGN JIHVAMULIYA

        # Quotations and text marking
        0x2308,  # LEFT CEILING
        0x2309,  # RIGHT CEILING
        0x230A,  # LEFT FLOOR - request from Dan
        0x230B,  # RIGHT FLOOR - request from Dan
        0x231C,  # TOP LEFT CORNER
        0x231D,  # TOP RIGHT CORNER
        0x231E,  # BOTTOM LEFT CORNER - used by Steve
        0x231F,  # BOTTOM RIGHT CORNER - used by Steve
        # 0x2E22,  # TOP LEFT HALF BRACKET - not in Charis
        # 0x2E23,  # TOP RIGHT HALF BRACKET - not in Charis
        # 0x2E24,  # BOTTOM LEFT HALF BRACKET - request from Steve - not in Charis
        # 0x2E25,  # BOTTOM RIGHT HALF BRACKET - request from Steve - not in Charis
        0xF130,  # FONT BASELINE AND SIDE-BEARING MARKER LEFT
        0xF131,  # FONT BASELINE AND SIDE-BEARING MARKER RIGHT

        # Footnote callers
        # 0x2756,  # BLACK DIAMOND MINUS WHITE X - suggested by Dan - not in Charis

        # Glottal
        0x02BC,  # MODIFIER LETTER APOSTROPHE
        0x02C0,  # MODIFIER LETTER GLOTTAL STOP
        # 0xA78B,  # LATIN CAPITAL LETTER SALTILLO
        0xA78C,  # LATIN SMALL LETTER SALTILLO
        # 0x0241,  # LATIN CAPITAL LETTER GLOTTAL STOP - maybe only for Latin orthographies
        0x0242,  # LATIN SMALL LETTER GLOTTAL STOP - maybe only for Latin orthographies
        0x0294,  # LATIN LETTER GLOTTAL STOP

        # Misc
        0x2423,  # OPEN BOX

        # MacRoman not in Codepage 1252
        0x03A9,  # GREEK CAPITAL LETTER OMEGA

        # Variation Selectors
        # list(xrange(0xE0100, 0xE01EF)) # VARIATION SELECTOR-17..VARIATION SELECTOR-256 - non BMP characters not handled

        # Superscripted footnote callers
        0x2070,  # SUPERSCRIPT ZERO
        0x207B,  # SUPERSCRIPT MINUS
        0x207D,  # SUPERSCRIPT LEFT PARENTHESIS
        0x207E,  # SUPERSCRIPT RIGHT PARENTHESIS
    ] + \
        list(xrange(0x2074, 0x2079+1))  # SUPERSCRIPT FOUR..SUPERSCRIPT NINE

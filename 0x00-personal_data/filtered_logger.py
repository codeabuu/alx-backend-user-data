#!/usr/bin/env python3
'''function called filter_datum that
returns the log message obfuscated'''


import re


def filter_datum(fields, redaction, message, separator):
    '''use a regex to replace occurrences
    of certain field values'''
    return re.sub('({})[^{}]*'.format(separator.join(
        fields), separator), redaction, message)

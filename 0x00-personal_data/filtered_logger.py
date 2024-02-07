#!/usr/bin/env python3
'''function called filter_datum that
returns the log message obfuscated'''


import re
import logging


def filter_datum(fields, redaction, message, separator):
    '''use a regex to replace occurrences
    of certain field values'''
    return re.sub('({})=(.*?)(?={})'.format('|'.join(fields), separator),
            lambda match: match.group(1) + '=' + redaction, message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        '''constructor'''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format function for class"""
        record.msg = filter_datum(
                self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)

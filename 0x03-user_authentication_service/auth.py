#!/usr/bin/env python3
'''auth py methods'''


import bcrypt


def _hash_password(password: str) -> bytes:
    '''hashimg pwd method'''
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

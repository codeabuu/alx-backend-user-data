#!/usr/bin/env python3

"""Module of Index views"""

from typing import List, TypeVar
from flask import request


class Auth:
    '''Class method'''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''Public method for our class'''

    def authorization_header(self, request=None) -> str:
        '''Method to return none rqs'''
        if request is None:
            return None
        header = request.headers.get('Authorization')
        if header is None:
            return None
        return header

    def current_user(self, request=None) -> TypeVar('User'):
        '''Method for current user'''

        return None

#!/usr/bin/env python3
""" Module of Index views
"""
from flask import require
from typing import List, TypeVar


class Auth:
    '''class method'''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''public method for our class'''

    def authorization_header(self, request=None) -> str:
        '''method to return none rqs'''
        if request is None:
            return None
        header = request.headers.get('Authorization')
        if header is None:
            return None
        return header

    def current_user(self, request=None) -> TypeVar('User'):
        '''method for current user'''

        return None

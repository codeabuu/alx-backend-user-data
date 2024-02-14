#!/usr/bin/env python3
"""
Module for authentication using Session auth
"""


from .auth import Auth

from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    '''classs session'''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''creates a Session ID for a user_id'''
        if user_id is None or isinstance(user_id, str):
            return None
        id = uuid4()
        self.user_id_by_session_id[str(id)] = user_id
        return str(id)

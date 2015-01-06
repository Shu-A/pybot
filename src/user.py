#!/usr/bin/env python
# -*- coding:utf-8 -*-

class User(object):
    """
    Represents a participating user in the chat.

    id      : A unique ID for the user.
    options : An optional Hash of key, value pairs for this user.
    """
    def __init__(self, id, options = {}):
        self.id = id
        for k in (options or {}):
            pass


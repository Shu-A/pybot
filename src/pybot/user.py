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
        for k, v in (options or {}).iteritems():
            self.__dict__[k] = v
        if not self.__dict__.has_key('name'):
            self.name = str(self.id)


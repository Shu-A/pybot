#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

class Shell(Adapter):
    def send(self, envelope, *strings):
        if sys.platform is not 'win32':
            

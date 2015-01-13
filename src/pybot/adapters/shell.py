#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os, sys

if os.environ.get('HUBOT_SHELL_HISTSIZE'):
    history_size = int(os.environ.get('HUBOT_SHELL_HISTSIZE')
else:
    history_size = 1024


class Shell(Adapter):
    def send(self, envelope, *strings):
        if sys.platform is not 'win32':
            for string in strings:
                print "\x1b[01;32m%s\x1b[0m" % string
        else:
            for string in strings:
                print string

        self.repl.prompt()

    def emote(self, envelope, *strings):
        self.send(envelope, [ "* %s" for string in strings ]

    def reply(self, envelope, *strings):
        for string in strings:
            string = envelope.user.name + ': ' + string

        seld.send(envelope, strings)

    def run(self):
        stdin = sys.stdin
        stdout = sys.stdput

        self.repl = None
        pass

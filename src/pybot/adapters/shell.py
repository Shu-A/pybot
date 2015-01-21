#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os, sys

from pybot.adapter import Adapter

if os.environ.get('HUBOT_SHELL_HISTSIZE'):
    history_size = int(os.environ.get('HUBOT_SHELL_HISTSIZE'))
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
        self.send(envelope, [ "* %s" for string in strings ])

    def reply(self, envelope, *strings):
        for string in strings:
            string = envelope.user.name + ': ' + string

        seld.send(envelope, *strings)

    def run(self):

        history_file_path = ".hubot_history"
        try:
            f = open(history_file_path, 'r')
            history_lines = [ l[:-1] for l in f.readlines()[:history_size] ]
            f.close()
        except IOError:
            history_lines = []

        self.emit('connected')

        f = open(history_file_path, 'w')
        while True:
            line = raw_input('> ')
            if len(history_lines) >= history_size:
                history_lines.pop(0)
            history_lines.append(line)
            print history_lines

            if line == 'exit' or line == 'quit':
                self.robot.shutdown()
                break
            elif line == 'history':
                for history in history_lines:
                    print history
            else:
                user_id = int(os.environ.get('HUBOT_SHELL_USER_ID') or '1')
                user_name = os.environ.get('HUBOT_SHELL_USER_NAME') or 'Shell'
                options = { 'name': user_name, 'room': 'Shell' }
                user = self.robot.brain.user_for_id(user_id, options)
                sel.recieve = TextMessage(user, line, 'messageID')

        for line in history_lines:
            f.write(line + '\n')
        f.close()

        sys.exit(0)

    def close(self):
        pass

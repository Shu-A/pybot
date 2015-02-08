#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

from pybot.message import TextMessage

class Listener(object):
    """
    Listeners receive every message from the chat source and decide 
    if they wat to act no it.
    """
    def __init__(self, robot, matcher, callback):
        """
        Constructor.

        Args:
        robot   : A Robot instance.
        metcher : A Function that determines if this listener should trigger
                  the callback.
        callback: A Function that is triggered if the incoming message matches,
        """
        self.robot = robot
        self.matcher = matcher
        self.callback = callback

    def call(self, message):
        """
        Public:
        Determines if the listener likes the content of the message.
        If so, a Response built from the given Message is passed to
        the Listerner callback.

        Args:
        message : A Message instance.

        Returns a boolean of whether the matcher matched.
        """
        match = self.matcher(message)
        if match:
            if self.regex:
                self.robot.logger.debug("Message %s matched regex %s"
                                        % (message, regex))
            self.callback(self.robot.Response(self.robot, message, match))
            return True
        else:
            return False


class TextListener(Listener):
    """
    TextListeners recieve every message from the chat source and decide
    if they want to act on it.
    """
    def __init__(self, robot, regex, callback):
        """
        Constructor.

        Args:
        robot   : A Robot instance.
        regex   : A Regex that determines if this listener should trigger
                  the callback.
        callback: A Function that is triggered if the incoming message metches.
        """

        def matcher(message):
            if isinstance(message, TextMessage):
                return re.match(self.regex, message)

        super(TextListener, self).__init__(robot, regex, callback)
        self.robot      = robot
        self.regex      = regex
        self.callback   = callback
        self.matcher    = matcher(self)


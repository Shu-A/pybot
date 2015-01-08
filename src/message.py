#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

class Massage:
    """
    Represents an imcoming from the chat.
    """
    def __init__(self, user, done = False):
        """
        Constructor

        Args:
        user    : A User instance that sent the message.
        """
        self.user = user
        self.room = user.room

    def finish(self):
        """
        Indicates that no other Listener should be called on this object

        Returns nothing.
        """
        self.done = True


class TextMessage(Message):
    """
    Represents an incoming message from the chat.
    """
    def __init__(self, user, text, id):
        """
        Constructor

        Args:
        user    : A User instance that sent the message.
        text    : A String message.
        id      : A String of the message ID.
        """
        super(TextMessage, self).__init__(user)
        self.text = text
        self.id = id

    def match(self, regex):
        """
        Determines if the message mathces the given regex.

        Args:
        regex   : A Regex to check.

        REturns a Match object or None
        """
        return re.match(regex, self.text)

    def to_string(self):
        """
        String representation of a TextMessage

        Retuens the message text
        """
        return self.text


class ExterMessage(Message):
    """
    Represents an incoming user entrance notification.
    """

class LeaveMessage(Message):
    """
    Represents an incoming user exit notification
    """

class TopicMessage(Message):
    """
    Represents an incoming topic change notification.
    """

class CatchAllMessage(Message):
    """
    Represents a message that no matchers matched.
    """
    def __init__(self, message):
        """
        Constructor.

        Args:
        message : The original message.
        """
        self.message = message
        super(CatchAllMessage, self).__init__(self.message.user)


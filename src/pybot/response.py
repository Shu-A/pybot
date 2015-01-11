#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Response:
    """
    Responses are sent to mathching listeners. Messages know about the
    content and user that made the original message, and how to reply back to
    them.
    """
    def __init__(self, robot, message, match):
        """
        Constructor.

        Args:
        robot   : A Robot instance.
        message : A Message instance.
        match   : A Match object from the successful Regex match.
        """
        self.envelope = {
            room    : self.message.room,
            user    : self.message.user,
            message : self.message }

    def send(self, *strings):
        """
        Public:
        Posts a message back to the chat source

        Args:
        strings : One or more strings to be posted. The order of these
                  strings should be kept intact.

        Return nothing.
        """
        self.robot.adapter.send(self.envelope, strings)

    def emote(self, *strings):
        """
        Public:
        Posts an emote back to the chat source

        Agrs:
        strings : One or more strings to be posted. The order of these
                  strings should be kept intact.

        Returns nothing.
        """
        self.robot.adapter.emote(self.envelope, strings)

    def reply(self, *strings):
        """
        Public:
        Posts a message mentioning the current user.

        Agrs:
        strings : One or more strings to be posted. The order of these
                  strings should be kept intact.

        Returns nothing.
        """
        self.robot.adapter.reply(self.envelope, strings)

    def topic(self, *strings):
        """
        Public:
        Posts a topic changing message

        Agrs:
        strings : One or more strings to set as the topic of the room
                  the bot is in.

        Returns nothing.
        """
        self.robot.adapter.topic(self.envelope, strings)

    def play(self, *strings):
        """
        Public:
        Play a sound in the chat source

        Agrs:
        strings : One or more strings to be posted as sounds to play.
                  The order of these strings should be kept intact.

        Returns nothing.
        """
        self.robot.adapter.play(self.envelope, strings)

    def locked(self, *strings):
        """
        Public:
        pasts a message in an unlogged room

        Args:
        strings : One or more strings to be posted. The order of these
                  strings should be kept intact.
        
        Returns nothing.
        """
        self.robot.adapter.locked(self.envelope, strings)

    def random(self, items):
        """
        Public:
        Picks a random item from the given items.

        Args:
        items   : An Array of items

        Returns a random items
        """
        pass

    def finish(self):
        """
        Public:
        Tell the message to stop dispatching to listeners

        Returns nothing.
        """
        self.message.finish()

    def http(self, url, options):
        """
        Public:
        Creates a scoped http client with chainable methods for modifying
        the request. This doesn't actually make a request though.
        Once your request is assembled, you can call `get()`/`post()`/etc to
        send the reqeust.

        Returns a ScopedClient instance.
        """
        self.robot.http(url, options)


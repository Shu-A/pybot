#!/usr/bin/env python
# -*- coding:utf-8 -*-

from event_emitter import EventEmitter

class Adapter(EventEmitter):
    """
    An adapter is a specific interface to a chat source for robots.
    """
    def __init__(self, robot):
        """
        Constructor.

        Args:
        robot   : A Robot instance.
        """
        super(Adapter, self).__init__()
        self.robot = robot

    def send(self, envelope, *strings):
        """
        Public:
        Raw method for sending data back to the chat source. extend this.

        Args:
        envelope    : A Object with message, room and user details.
        strings     : One or more Strings for each message to send.

        Returns nothing.
        """
        raise NotImplementedError

    def emote(self, envelope, *strings):
        """
        Public:
        Raw method for sending emote data back to the chat source.
        Defaults as an alias for send

        Args:
        envelope    : A Object with message, room and user details.
        strings     : One or more Strings for each message to send.

        Returns nothing.
        """
        self.send(envelope, *strings)

    def reply(self, envelope, *strings):
        """
        PUblic:
        Raw method for building a reply and sending it back to the chat source.
        Extend this.

        envelope    : A Object with message, room and user details.
        strings     : One or more Strings for each reply to send.

        Returns nothing.
        """
        raise NotImplementedError

    def topic(self, envelope, *strings):
        """
        PUblic:
        Raw method for setting a topic on the chat source.
        Extend this.

        envelope    : A Object with message, room and user details.
        strings     : One or more Strings to set as the topic.

        Returns nothing.
        """
        raise NotImplementedError

    def play(self, envelope, *strings):
        """
        PUblic:
        Raw method for playing a sound in the chat source.
        Extend this.

        envelope    : A Object with message, room and user details.
        strings     : One or more Strings for each play message to send.

        Returns nothing.
        """
        raise NotImplementedError

    def run(self):
        """
        Public:
        Raw method for invokeing the bot to run.
        Extend this.

        Returns nothing.
        """
        raise NotImplementedError

    def close(self):
        """
        Public:
        Raw method for shutting the bot down.
        Extend this.

        Returns nothing.
        """
        raise NotImplementedError

    def recieve(self, message):
        """
        Public:
        Dispatch a recieve message to the robot.

        Returns nothing.
        """
        self.robot.recieve(message)

    def users(self):
        """
        Public:
        Get an Array of User objects stored in the brain.

        Returns an Array of User objects.
        """
        self.robot.logger.warning("self.users() is going to be deprecated ",
            "in 3.0.0 use self.robot.brain.users()")
        self.robot.brain.users()

    def user_for_id(self, id, options):
        """
        Public:
        Get a User object given a unique identifier.

        Returns a User instance of the specified user.
        """
        self.robot.logger.warning("self.user_for_id() is going to be ",
            "deprecated in 3.0.0 use self.robot.brain.user_for_id()")
        self.robot.brain.user_for_id()

    def user_for_name(self, name):
        """
        Public:
        Get a User object given a name.

        Returns a User instance for the user with specified name.
        """
        self.robot.logger.warning("self.user_for_name() is going to be ",
            "deprecated in 3.0.0 use self.robot.brain.user_for_name()")
        self.robot.brain.user_for_name()

 
    def users_for_raw_fuzzy_name(self, fuzzy_name):
        """
        Public:
        Get all users whose names match fuzzy_name. Currently, match means
        'starts with', but this could be extended to match initials,
        nickename, etc.

        Returns an Array of User instances mathcing the fuzzy name.
        """
        self.robot.logger.warning("self.users_for_raw_fuzzy_name() ",
            "is going to be deprecated in 3.0.0 use ",
            "self.robot.brain.users_for_raw_fuzzy_name()")
        self.robot.brain.users_for_raw_fuzzy_name()

 
    def users_for_fuzzy_name(self, fuzzy_name):
        """
        Public:
        If fuzzy_name is an exact match for a user, returns an array with
        just that user. Otherwise, returns an array of all users for which
        fuzzy_name is a raw fuzzy match (see users_for_raw_fuzzy_name).

        Returns an Array of User instances matching the fuzzy name.
        """
        self.robot.logger.warning("self.users_for_fuzzy_name() is going to be",
            "deprecated in 3.0.0 use self.robot.brain.users_for_fuzzy_name()")
        self.robot.brain.users_for_fuzzy_name()

 
    def http(self, url):
        """
        Public:
        Creates a scoped http client with chainable methods for medifying
        the request. This doesn't actually make a request though.
        Once your request is assembled, you can call `get()`/`post()`/etc to
        send the reqeust.

        Returns a ScopeClient instance.
        """
        self.robot.logger.warning("self.http() is going to be",
            "deprecated in 3.0.0 use self.robot.brain.http()")
        self.robot.brain.http()


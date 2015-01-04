#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import logging
import re

from event_emitter import EventEmitter

HUBOT_DEFAULT_ADAPTERS = [ 'campire', 'shell' ]

HUBOT_DOCUMENTATION_SECTIONS = [
    'description',
    'dependencies',
    'configuration',
    'commands',
    'notes',
    'auther',
    'authers',
    'examples',
    'tags',
    'urls'
]


class robot(object):
    """
    Robots recieve message from a chat source (Campfire, irc, etc), and
    dispatch them to matching listeners.
    """

    def __init__(self, adapter_path, adapter, httd, name='Hubot'):
        """
        Constructor.

        Attributes:
            adapter_path: A String of the path to local adapters.
            adapter     : A String of the adapter name.
            httpd       : A Boolean whether to enable the HTTP daemon.
            name        : A String of the robot name, defaults to Hubot.
    
        Returns nothing.
        """
        self.name       = name
        self.events     = EventEmitter()
        self.brain      = Brain(self)
        self.alias      = false
        self.adapter    = null
        self.response   = Response
        self.commands   = []
        self.listeners  = []
        self.logger     = logger.getLogger()
        self.logger(level=os.environ.get(HUBOT_LOG_LEVEL or 'info')
        self.ping_interval_id = null

        self.parse_version()
        if httpd:
            self.setup_express()
        else:
            self.setup_null_router()

        self.load_adapter(adapter_path, adapter)

        self.adapter_name = adapter
        self.error_handlers = []

        ## TODO: Write this code as Python
        """
        @on 'error', (err, msg) =>
            @invokeErrorHandlers(err, msg)
        process.on 'uncaughtException', (err) =>
            @emit 'error', err
        """

    def hear(self, regex, callback):
        """
        Public:
        Adds a Listener that attempts to match incoming messages based on
        a Regex.

        Args:
        regex   : A Regex that determines if the callback should be called.
        callback: A Function that is called with a Response object.

        Returns nothing.
        """
        self.listeners.append(TextListener(self, regex, callback))

    def respond(self, regex, callback):
        """
        Public:
        Adds a Listener that attempts to match incoming messages directed
        at the robot based on a Regex. All regexes treat patterns like they
        begin with a '^'

        Args:
        regex   : A Regex that determines if the callback should be called.
        callback: A Function that is called with a Response object.

        Returns nothing.
        """
        re = str(regex).split('/')
        modifiers = re[1:-1]

        ## TODO: Check "is this evaluation collect?"
        if re[0] and re[0][0] is '^':
            self.logger.warning("Anchors don't work well with respond,", 
                                "perhaps you want to use 'hear'")
            self.logger.warning("The regex in question was %s" % str(regex))

        pattern = re.join('/')
        name = re.sub(r'[-[\]{}()*+?.,\\^$|#\s]', '\\$&', self.name)

        if self.alias:
            alias = re.sub(r'[-[\]{}()*+?.,\\^$|#\s]', '\\$&', self.alias)
            new_regex = 
        else:
            new_regex = 

        self.listeners.append(TextListener(self, new_regex, callback)

    def enter(self, callback):
        """
        Public:
        Adds a Listener that triggers when anyone enters the room.

        Args:
        callback    : A Function that is called with a Response object.

        Returns nothing.
        """
        self.listeners.append(Listener(
            self,
            lambda(msg): isinstance(msg, EnterMessage),
            callback)

    def leave(self, callback):
        """
        Public:
        Adds a Listener that triggers when anyone leaves the room.

        Args:
        callback    : A Function that is called with a Response object.

        Returns nothing.
        """
        self.listeners.append(Listener(
            self,
            lambda(msg): isinstance(msg, LeaveMessage)),
            callback)

    def topic(self, callback):
        """
        Public:
        Adds a Listener that triggers when anyone changes the topic.

        Args:
        callback    : A Function that is called with a Response object.

        Returns nothing.
        """
        self.listeners.append(Listener(
            self,
            lambda(msg): isinstance(msg, TopicMessage),
            callback)

    def error(self, callback):
        """
        Public:
        Adds an error handler when an uncaught exception or user emitted
        error event occurs.

        Args:
        callback    : A Function that is called with the error object.

        Return nothing.
        """
        self.error_handlers.append(callback)

    def invoke_error_handlers(self, err, msg):
        """
        Calls and passes any registered error handlers for unhandled exceptions
        or user emitted error events.

        Args:
        err     : An Error object.
        msg     : An optional Response object that generated the error

        Returns nothing.
        """
        self.logger.error(err.stack)
        for error_handler in self.error_handlers:
            try:
                error_handler(err, msg)
            except:
                self.logger.error("while invoking error handler: %s\n%s" %
                                  (err, err.stack))

    def catch_all(self, callback):
        pass

    def recieve(self, message):
        pass

    def load_file(self, path, file):
        pass

    def load(self, path):
        pass

    def load_hubot_scripts(self, path, scripts):
        pass

    def load_external_scripts(self, packages):
        pass

    def setup_express(self):
        pass

    def setup_null_router(self):
        pass

    def load_adapter(self, path, adapter):
        pass

    def help_commands(self):
        pass

    def parse_help(self, path):
        pass

    def send(self, user, *strings):
        """
        Public:
        A helper send function which delegates to the adapter's send function.

        Args:
        user    : A User instance.
        string  : One or more String for each message to send.

        Returns nothing.
        """
        self.adapter.send(user, strings)

    def reply(self, user, *strings):
        """
        Public:
        A helper reply function which delegates to the adapter's reply
        function.

        Args:
        user    : A User instance.
        string  : One or more Strings for each message to send.

        Returns nothing.
        """
        self.adapter.reply(user, strings)

    def message_room(self, room, *strings):
        """
        Public:
        A helper send function to message a room that the robot is in.

        Args:
        room    : String designating the room to message.
        strings : One or more Strings for each message to send.

        Returns nothing.
        """
        user = {room: room }
        self.adapter.send(user, strings)

    def on(self, event, *args):
        ## TODO: Check is this args comment right?
        """
        Public:
        A wrapper around the EventEmitter API to make usage sematicly better.

        Args:
        event   : The event name.
        listener: A Function that is called with the event parameter
                  when event happens.

        Returns nothing.
        """
        self.events.on(event, args)

    def emit(self, event, *args):
        """
        Public:
        A wrapper around the EventEmitter API to make usage semanticly better.

        Args:
        event   : The event name.
        *args   : Arguments emitted by the event
        """
        self.events.emit(event, agrs)

    def run(self):
        """
        Public:
        Kick off the event loop for the adapter

        Returns nothing.
        """
        self.emit("running")
        self.adapter.run()

    def shutdown(self):
        """
        Public:
        Gracefully shutdown the robot process

        Returns nothing.
        """
        if self.ping_interval_id:
            clear_interval(self.ping_interval_id)
        self.adapter.close()
        self.brain.close()

    def perse_version(self):
        """
        ### Not implemented !!! ###

        Public:
        The version of Hubot from npm

        Returns a String of the version number.
        """
        pass

    def http(self, url, options):
        """
        ### Not implemented !!! ###

        Public:
        Creates a scoped http client with chainable methods for medifying the
        request. This doesn't actually make a request though.
        Once your the request os assembled, you can call `get()`/`post()`/etc
        to send the request.

        Args:
        url     : String URL to access.
        options : Optional options to pass on to the client.

        Exmples:

            robot.http("http://example.com")
                # set a single header
                .header('Authorization', 'bearer abcdef')

                # set multiple headers
                .headers(Authorization: 'bearer abcdef', Accept: 'application')

                # add URI query parameters
                .query(a: 1, b: 'foo & bar')

                # make the actual request
                .get() (err, res, body) ->
                  console.log body

                # or , you can POST data
                .post(data) (err, res, body) ->
                  console.log body

            # Can also set options
            robot.http("https://example.com", {rejectUnauthorized: false})

        Returns a ScopedClient instance.
        """
        pass

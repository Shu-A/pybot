#!/usr/bin/env python
# -*- coding:utf-8 -*-

from event_emitter import EventEmitter

class Brain(EventEmitter):
    """
    Represents somewhat persistent storage for the robot. Extend this.

    Returns a new Brain with no external storage.
    """
    def __init__(self, robot):
        self.data = {
            users   : {}
            _private: {}
            }

        self.auto_save = True

        robot.on("running", lambda: self.reset_save_interval(5)

    def set(self, key, value):
        """
        Public:
        Store key-value pair under the private namespace and extend
        existing self.data before emitting the 'loaded' event.

        Returns the instance for chaining.
        """
        pass

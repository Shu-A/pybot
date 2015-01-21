#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import threading

from event_emitter import EventEmitter

class Brain(EventEmitter):
    """
    Represents somewhat persistent storage for the robot. Extend this.

    Returns a new Brain with no external storage.
    """
    def __init__(self, robot):
        super(Brain, self).__init__()
        self.data = {
            'users'     : {},
            '_private'  : {}
            }

        self.auto_save = True
        self.save_interval = None
        self.stop_event = threading.Event()

        robot.on("running", lambda: self.reset_save_interval(5))

    def set(self, key, value):
        """
        Public:
        Store key-value pair under the private namespace and extend
        existing self.data before emitting the 'loaded' event.

        Returns the instance for chaining.
        """
        ## Memo: Check object instance or not ?
        pass

    def get(self, key):
        """
        Public:
        Get value by key from the private namespace in self.data
        or return null if not found.

        Returns the value.
        """
        if self.data._private.has_key(key):
            return self.data._private[key]
        else:
            return None

    def remove(self, key):
        """
        Public:
        Remove value by key from the private namespace in self.data
        if it exists

        Returns the instance for chaining.
        """
        if self.data._private.has_key(key):
            self.data._private.pop(key)

        return self

    def save(self):
        """
        Public:
        Emits the 'save' event so that 'brain' scripts can handle persisting.

        Returns nothing.
        """
        self.emit('save', self.data)

    def close(self):
        """
        Public:
        Emits the 'close' event so that 'brain' scripts can handle closing.

        Returns nothing.
        """
        self.clear_interval()
        self.save()
        self.emit('close')

    def set_auto_save(self, enabled):
        """
        Public:
        Enable or disable the automatic saving

        enabled : A boolean whether to autosave or not

        Returns nothing.
        """
        self.auto_save = enabled

    def reset_save_interval(self, seconds):
        """
        Public:
        Reset the interval between save function calls.

        seconds : An Integer of seconds between saves.

        Returns nothing.
        """
        if self.save_interval:
            self.clear_interval()
        if self.auto_save:
            self.set_interval(self.save, seconds)

    def set_interval(self, callback, delay):
        def _target():
            while not self.stop_event.is_set():
                time.sleep(delay)
                callback()

        self.thread = threading.Thread(target=_target)
        self.thread.start()
        self.save_interval = True

    def clear_interval(self):
        self.stop_event.set()
        self.thread.join()
        self.save_interval = False

    def merge_data(self, data):
        """
        Public:
        Merge keys loaded from a DB against the in memory representation.

        Returns nothing.

        Caveates:
        Deeply nested structures don't merge well.
        """
        for key in (data or {}):
            self.data[key] = data[key]

        self.emit('loaded', self.data)

    def users(self):
        """
        Public:
        Get an Array of User objects stored in the brain.

        Returns an Array of User objects.
        """
        return self.data.users

    def user_for_id(self, id, options):
        """
        Public:
        Get a User object given a unique identifier.

        Returns a User instance of the specified user.
        """
        user = self.data['users'][id]
        if not user:
            user = User(id, options)
            self.data['users'][id] = user

        if (options
            and options.has_key('room')
            and (not user.room or user.room is not options.has_key['room'])):
            user = User(id, options)
            self.data.users[id] = user

        return user

    def user_for_name(self, name):
        """
        Public:
        Get a User object given a name.

        Returns a User instance for the user with the specified name.
        """
        result = None
        lower_name = name.lower()
        for key in (self.data.users or {}):
            user_name = self.data.users[key]['name']
            if user_name and str(user_name).lower() is lower_name:
                result = self.data.users[key]

        return result

    def users_for_raw_fuzzy_name(self, fuzzy_name):
        """
        Public:
        Get all users whose names match fuzzy_name. Currently, match
        means 'starts with', but this could be extended to match initials,
        nicknames, etc.

        Returns an Array of User instances matching the fuzzy name.
        """
        lower_fuzzy_name = fuzzy_name.lower()
        users = []
        for key, user in (self.user or {}):
            if (user.name.lower().index(lower_fuzzy_name) == 0
                and user.name.lower().count(lower_fuzzy_name)):
                    users.append(user)

        return users

    def users_for_fuzzy_name(self, fuzzy_name):
        """
        Public:
        If fuzzy_name is an exact match for a user, returns an array with
        just that user. Otherwise, returns an array of all users for which
        fuzzy_name is a raw fuzzy match (see users_for_raw_fuzzy_name)

        Returns an Array of User instances matching the fuzzy name.
        """
        matchd_users = self.users_for_raw_fuzzy_name(fuzzy_name)
        lower_fuzzy_name = fuzzy_name.lower()
        for user in matched_users:
            if user.name.lower() is lower_fuzzy_name:
                return [user]

        return matched_users

    def extend(self, obj, *sources):
        """
        Private:
        Extend obj with objects passed as additional args.

        Returns the original object with updated changes.
        """
        for source in sources:
            for key, val in source.items():
                ojb[key] = val

        return obj


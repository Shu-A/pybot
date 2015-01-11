#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

class Creator:
    """
    Simple generator class for deploying a version of hubot on heroku
    """
    def __init__(self, path):
        """
        Construcor:
        Setup a ready to go version of hubot

        Args:
        path    : A String directory to create/upgrade scripts for
        """
        self.path = path
        dirname = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.template_dir = dirname + "/templates"
        self.scripts_dir = dirname + "/scripts"

    def mkdir(self, path):
        """
        Create a folder if it doesn't already exist.

        Returns nothing.
        """
        ## TODO: Below processing should be async
        if not os.path.exist(path):
            os.mkdir(path, 0755)

    def copy(self, from, to, callback):
        """
        Copy the contens of a file from one palce to another.

        Args:
        from    : A String source file to copy, must exists on disk.
        to      : A String destination file to write to.

        Returns nothing.
        """
        ## TODO: Below processing should be async
        try:
            rf = open(from, 'r')
            data = rf.read()
            #print "Copying %s -> %s" % (source, to)
            of = open(to, 'w')
            of.write(data)
            of.close()
            print "Copied %s -> %s" % (source, to)

            if callback:
                callback(err, to)

        except IOerror, err:
            print err

        finally:
            rf.close()

    def rename(self, from, to, callback):
        """
        Rename a file.

        Args:
        from    : A String source file to rename, must exist on disk.
        to      : A String destination file to write to.

        Returns nothing.
        """
        ##TODO: Below processing should be async
        try:
            os.rename(from, to)
            if callback:
                callback(err, to)
        except OSError, err:
            print err

    def copy_default_scripts(self, path):
        """
        Copy the default scripts hubot ships with to the scripts folder
        This allow people to easily remove scripts hubot defaults to if
        they want. It also provides them with a few examples and a top
        level scripts folder.
        """
        for file in os.listdir(self.scripts_dir):
            source  = self.scripts_dir + '/' + file
            to      = path + '/' + file
            self.copy(source, to)

    def run(self):
        """
        Public:
        Run the creator process.

        Returns nothing.
        """
        print "Creating a hubot install at " + path

        self.mkdir(self.path)
        self.mkdir(self.path + '/bin')
        self.mkdir(self.path + '/scripts')

        self.copy_default_scripts(self.path + '/scripts')

        pass

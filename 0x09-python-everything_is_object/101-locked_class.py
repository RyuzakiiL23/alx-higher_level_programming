#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    def __setattr__(self, name, value):
        if not hasattr(self, 'first_name') and name != 'first_name':
            raise AttributeError("Cannot create new instance attributes")
        super().__setattr__(name, value)

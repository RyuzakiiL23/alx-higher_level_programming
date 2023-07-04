#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    def __setattr__(self, name, value):
        super().__setattr__(name, value)

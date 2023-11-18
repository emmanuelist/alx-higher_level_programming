#!/usr/bin/python3
"""
Module Docs
"""
from json import dumps, loads
from os.path import isfile
import csv
import turtle
from random import randint, shuffle, randrange


class Base:
    """
    Class Docs
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Function Docs
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod

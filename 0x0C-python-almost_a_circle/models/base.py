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
def to_json_string(list_dictionaries):
        """
        Function Docs
        """

        if type(list_dictionaries) is list:
            if len(list_dictionaries) == 0:
                return dumps([])
            else:
                return dumps(list_dictionaries)
        elif list_dictionaries is None:
            return dumps([])

    @classmethod
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
def save_to_file(cls, list_objs):
        """
        Function Docs
        """

        if list_objs is None:
            final_list = []
        else:
            final_list = [i.to_dictionary() for i in list_objs]
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as f:
            f.write(Base.to_json_string(final_list))

    @staticmethod
def from_json_string(json_string):
        """
        Function Doc
        """

        if type(json_string) is str:
            if len(json_string) == 0:
                return []
            else:
                return loads(json_string)
        elif json_string is None:
            return []

    @classmethod

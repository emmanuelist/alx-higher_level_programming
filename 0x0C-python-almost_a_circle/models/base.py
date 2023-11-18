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
def create(cls, **dictionary):
        """
        Function Doc
        """

        if cls.__name__ == "Rectangle":
            dummy_obj = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_obj = cls(1)
        else:
            dummy_obj = cls()
            return dummy_obj
        dummy_obj.update(**dictionary)
        return dummy_obj

    @classmethod
def load_from_file(cls):
        """
        Function Doc
        """

        filename = "{}.json".format(cls.__name__)
        obj_list = []
        if isfile(filename):
            with open(filename, "r") as f:
                line = f.readline()
                final_list = Base.from_json_string(line)
            for i in final_list:
                class_created = cls.create(**i)
                obj_list.append(class_created)
        return obj_list

    @classmethod
def save_to_file_csv(cls, list_objs):
        """
        function docs
        """

        filename = "{}.csv".format(cls.__name__)
        with open(filename, mode='w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',',
                                    quotechar='"',
                                    quoting=csv.QUOTE_MINIMAL)
            for i in list_objs:
                i_list = cls.to_list(i)
                csv_writer.writerow(i_list)

    @classmethod

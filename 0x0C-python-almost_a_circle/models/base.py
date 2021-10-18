#!/usr/bin/python3
"""
Defines a class Base
"""

import json


class Base:
    """Representation of a base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON of a dictionary """
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        return json.dumps(list_dictionaries)

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
        """returns the JSON string representation of a list of dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        lo = []
        if list_objs is not None:
            for i in list_objs:
                lo.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(lo))

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes of the dict """
        if cls.__name__ == "Rectangle":
            temp = cls(width=6, height=9)
        if cls.__name__ == "Square":
            temp = cls(size=69)
        temp.update(**dictionary)

        return temp

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        temp = []
        try:
            with open("{}.json".format(
                    cls.__name__), "r", encoding='utf-8') as f:
                temp2 = cls.from_json_string(f.read())
        except:
            return []
        for i in temp2:
            temp.append(cls.create(**i))
        return temp

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ lol i didnt do dis """
        pass

    @classmethod
    def load_from_file_csv(cls):
        """ I dont like unit tests"""
        pass

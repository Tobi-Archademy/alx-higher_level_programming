#!/usr/bin/python3
"""
Defines a class rectangle
"""
from models.base import Base

class Rectangle(Base):
    """Representation of a rectangle that inherits from a base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization"""
        super().__init__(id)
        """calling the id instance from the Base superclass"""

        self.width = width
        self.height = height
        self.x =  x
        self.y = y


    @property
    def width(self):
        """getter width"""
        self.__width

    @width.setter
    def width(self, value):
        """width setter, gets validated"""
        if type(value) is not int:
            raise TypeError("width must be  an integer")
        if  value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter height"""
        self.__height

    @height.setter
    def height(self, value):
        """height setter, gets validated"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if  value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter x"""
        self.__x

    @x.setter
    def x(self, value):
        """x setter, gets validated"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if  value < 0:
            raise ValueError("x must be >= 0")
        self.__x =  value

    @property
    def y(self):
        """getter y"""
        self.__y

    @y.setter
    def y(self, value):
        """y setter, gets validated"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if  value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

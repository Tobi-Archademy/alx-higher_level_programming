#!/usr/bin/python3
''' Define a class Square. '''
class Square:
    ''' Represent a class Square '''
    def __init__(self, size=0):
        self.__size = size
        """Initialize a new Square method.
        
        Args:
            __size (int): The __size of the new square.
        """
    @property
    def size(self):
        return self.__size

    ''' Initialize an area of the setter method.
    Args:
        self: calculating the size of the Square.
        value: accessing the type of the value of Square.
    '''
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    ''' Initialize an area of the Square method.
    Args:
        area: calculating the area of the size of Square.
    '''
    def area(self):
        return self.__size ** 2

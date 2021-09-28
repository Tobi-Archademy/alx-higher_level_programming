#!/usr/bin/python3
''' Define a class Square. '''


class Square:
    """Square class that calculates the area of a sqare,
    has a getter and setter method"""

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
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    ''' Initialize an area of the Square method.
    Args:
        area: calculating the area of the size of Square.
    '''
    def area(self):
        return self.__size ** 2

    ''' Initialize a method that prints size of Square to stdout.'''
    def my_print(self):
        i = 0
        j = 0
        if self.__size == 0:
            print()
        else:
            while (i < self.__size):
                j = 0
                while (j < self.__size):
                    print("#", end='')
                    j += 1
                print()
                i += 1

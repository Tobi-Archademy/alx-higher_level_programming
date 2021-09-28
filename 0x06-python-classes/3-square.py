#!/usr/bin/python3
''' Define a class Square. '''


class Square:
    ''' Represent a class Square '''

    def __init__(self, size=0):
        """Initialize a new Square method.

        Args:
            __size (int): The __size of the new square.
        """
        if not str(size).isdigit():
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    '''Return the current area of the square.'''
    def area(self):
        return int(self.__size) ** 2

#!/usr/bin/python3
''' Define a class Square. '''
class Square:
    """Square class that calculates the area of
    a sqare, has a getter and setter method"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position


    ''' Initialize an area of the Square method.
    Args:
        area: calculating the area of the size of Square.
    '''
    def area(self):
        return self.__size ** 2


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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if ((len(value) != 2) or
            (type(value) is not tuple) or
            (type(value[0]) is not int) or (type(value[1]) is not int) or
                (value[0] < 0) or (value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


    ''' Initialize a method that prints size of Square to stdout.'''
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__size + self.__position[0]):
                    if j < self.__position[0]:
                        print(" ", end='')
                    else:
                        print("#", end='')
                print()

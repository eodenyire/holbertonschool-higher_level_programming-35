#!/usr/bin/python3
"""
New class Square
"""


class Square:
    """ Defines a Square """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Define area of square"""
        return (self.__size ** 2)

    def my_print(self):
        """ Prints in stdout the square with the character # """
        if self.size == 0:
            print("")
        else:
            for i in range(0, self.position[1]):
                print("")
            for i in range(0, self.size):
                for j in range(0, self.position[0]):
                    print(" ", end="")
                for j in range(0, self.size):
                    print("#", end="")
                print("")

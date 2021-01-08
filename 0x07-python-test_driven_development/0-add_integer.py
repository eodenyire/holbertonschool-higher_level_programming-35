#!/usr/bin/python3
""" Function that adds two integers """


def add_integer(a, b=98):
    """ Add integer function """

    if type(a) is int or type(a) is float:
        pass
    else:
        raise TypeError("a must be an integer")

    if type(b) is int or type(b) is float:
        pass
    else:
        raise TypeError("b must be an integer")

    return (a + b)

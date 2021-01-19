#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry
""" New class """


class Rectangle(BaseGeometry):
    """ New class Rectangle that inherist from Base Geometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

#!/usr/bin/python3

"""Define class with private __nb_objects """
class Base:


    """Base Class with __nb_objects as private class attribute"""
    
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Base Instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            
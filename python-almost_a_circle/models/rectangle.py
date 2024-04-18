#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    """
    A class that represents a rectangle.

    Attributes:
        id (int): The unique identifier for the rectangle.
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's top-left corner.
        y (int): The y-coordinate of the rectangle's top-left corner.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle object with the specified width, height, x-coordinate,
        y-coordinate, and optional identifier.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's top-left corner. Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's top-left corner. Defaults to 0.
            id (int, optional): The unique identifier for the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Returns the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            ValueError: If the new width is less than or equal to 0.
        """
        if value <= 0:
            raise ValueError("Width must be positive")
        self.__width = value

    @property
    def height(self):
        """
        Returns the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            ValueError: If the new height is less than or equal to 0.
        """
        if value <= 0:
            raise ValueError("Height must be positive")
        self.__height = value

    @property
    def x(self):
        """
        Returns the x-coordinate of the rectangle's top-left corner.

        Returns:
            int: The x-coordinate of the rectangle's top-left corner.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the x-coordinate of the rectangle's top-left corner.

        Args:
            value (int): The new x-coordinate of the rectangle's top-left corner.

        Raises:
            ValueError: If the new x-coordinate is less than 0.
        """
        if value < 0:
            raise ValueError("X must be non-negative")
        self.__x = value

    @property
    def y(self):
        """
        Returns the y-coordinate of the rectangle's top-left corner.

        Returns:
            int: The y-coordinate of the rectangle's top-left corner.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y-coordinate of the rectangle's top-left corner.

        Args:
            value (int): The new y-coordinate of the rectangle's top-left corner.

        Raises:
            ValueError: If the new y-coordinate is less than 0.
        """
        if value < 0:
            raise ValueError("Y must be non-negative")
        self.__y = value
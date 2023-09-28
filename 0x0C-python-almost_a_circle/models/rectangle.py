#!#usr/bin/python3
"""
Defines a class 'Rectangle'
subclass that inherits the superclass Base
"""

from models.base import Base


class Rectangle(Base):
    """
    Class attributes:
        size
    Methods Inherited:
        Base.init(self, id=None)
        Rectangle.init(self, width, height, x=0, y=0, id=None)
        update(self, *args,**kwargs)
        area(self)
        display(self)
    Methods:
        __init(self, width, height, x=0, y=0, id=None)
        __str__(self)
        area(self)
        to_dictionary(self)
        update(self, *args, **kwargs)
    getters:
        width(self) (x)
        height(self)  (y)
    setters:
        width(self, value) x(self, value)
        height(self,value) y(self, value)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialize attributes
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns Rectanlge's width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Returns width value of Rectangle"""
        if type(value) != int:
            raise TypeError("Width must be an intenger")
        if value <= 0:
            raise ValueError("Width must be > 0")

        self.width = value

    @property
    def height(self):
        """Returns the Rectangle's width"""
        return self.__height

    @height.setter
    def height(self, value):
        """Returns the height value of Rectangle"""
        if type(value) != int:
            raise TypeError("height must be an intenger")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value

    @property
    def y(self):
        if type != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

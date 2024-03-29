#!/usr/bin/python3
"""
    Rectangle module
    Class: Rectangle
"""


class Rectangle:
    """
        Rectangle class
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
            Object instace initialization method
        """
        self.width, self.height = width, height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
            width getter method
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            width setter method
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            height getter method
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            height setter method
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            Computes area of rectangle instance
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            Computes perimeter of rectangle instance
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
            String representation of rectangle instance
        """
        rec_str = ""
        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    rec_str += str(self.print_symbol)
                if i != self.__height - 1:
                    rec_str += "\n"
        return rec_str

    def __repr__(self):
        """
            Returns official string of rectangle instance
        """
        return f"Rectangle({self.__width}, {self.__height})"

    @staticmethod
    def __del__():
        """
            Print text and reduce number of instances when an class instance
            is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            Compares the area of two Rectangle instances
            Args:
                @rect_1: first Rectangle object
                @rect_2: second Rectangle object
            Return: instance with the greatest area
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

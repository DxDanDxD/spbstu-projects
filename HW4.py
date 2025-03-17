class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __getattr__(self, name):
        return "This attribute is not available"

class Rectangle:
    __slots__ = ['width', 'height']

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __setattr__(self, name, value):
        if name not in self.__slots__:
            raise AttributeError("Local attributes are not allowed")
        super().__setattr__(name, value)
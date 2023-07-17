#!/usr/bin/python3
"""The square object"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiating the class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Adjusting str special method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """size getter"""
        return self.width
    
    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """updating the square class"""
        attr_list = ["id", "size", "x", "y"]
        if args:
            i = 0
            for arg in args:
                if i >= len(args):
                    return
                self.__setattr__(attr_list[i], arg)
                i += 1
        else:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        """returns the dict representation of a square"""
        dict = {"id": self.id, "x": self.x, "size": self.width, "y": self.y}
        return dict

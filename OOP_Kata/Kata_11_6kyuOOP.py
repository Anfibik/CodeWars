"""https://www.codewars.com/kata/587e1ef6f1a2534bbe0001ef/train/python"""


class DimensionsOutOfBoundError(Exception):
    pass


class Package(object):
    L_MIN, L_MAX = 0, 350
    W_MIN, W_MAX = 0, 300
    H_MIN, H_MAX = 0, 150
    TW_MIN, TW_MAX = 0, 40

    def __init__(self, length, width, height, weight):
        self.verify_length(length)
        self.verify_width(width)
        self.verify_height(height)
        self.verify_weight(weight)

        self.__length = length
        self.__width = width
        self.__height = height
        self.__weight = weight

    @classmethod
    def verify_length(cls, length):
        if length < cls.L_MIN or length > cls.L_MAX:
            raise DimensionsOutOfBoundError(f"Package length=={length} out of bounds, should be: 0 < length <= {cls.L_MAX}")

    @classmethod
    def verify_width(cls, width):
        if width < cls.W_MIN or width > cls.W_MAX:
            raise DimensionsOutOfBoundError(f"Package width=={width} out of bounds, should be: 0 < width <= {cls.W_MAX}")

    @classmethod
    def verify_height(cls, height):
        if height < cls.H_MIN or height > cls.H_MAX:
            raise DimensionsOutOfBoundError(f"Package height=={height} out of bounds, should be: 0 < height <= {cls.H_MAX}")

    @classmethod
    def verify_weight(cls, weight):
        if weight < cls.TW_MIN or weight > cls.TW_MAX:
            raise DimensionsOutOfBoundError(f"Package weight=={weight} out of bounds, should be: 0 < weight <= {cls.TW_MAX}")

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.verify_length(length)
        self.__length = length

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.verify_width(width)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.verify_height(height)
        self.__height = height


    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def volume(self):
        return self.__length * self.__width * self.__height


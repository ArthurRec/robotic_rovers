from logger import logger

from src.core.enums.direction import DirectionEnum
from src.core.errors.direction import NotValidDirectionError, DirectionTypeError


class NonNegative:

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Cannot be negative.')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class NonNegativeInt(NonNegative):

    def __init__(self, val=0):
        self.default = val

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, self.default)

    def __set__(self, obj, value):
        self.validate(value)
        obj.__dict__[self.name] = value

    def validate(self, value):
        if not isinstance(value, int):
            raise AttributeError(f"value of '{self.name}' must be a number")
        if value < 0:
            raise ValueError(f"value of '{self.name} cannot be negative")


class Direction:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if isinstance(value, str):
            if value not in DirectionEnum.relations.keys():
                raise NotValidDirectionError(f"Bad direction has been set: {value}")
            else:
                instance.__dict__[self.name] = value
                logger.info(f"New direction has been set for rover: {instance.__dict__[self.name]}")
        else:
            raise DirectionTypeError()

    def __set_name__(self, owner, name):
        self.name = name

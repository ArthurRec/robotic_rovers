from dataclasses import dataclass

from src.core.utils.descriptors import NonNegativeInt


# class SlottedPlateau:
#     def __init_subclass__(cls, **kwargs):
#         cls.__init__(cls)


@dataclass  # (slots=True)
class Plateau:  # (SlottedPlateau, x=field(default=NonNegativeInt())):
    """ """

    # __slots__ = ['x', 'y']

    x: int = NonNegativeInt()
    y: int = NonNegativeInt()

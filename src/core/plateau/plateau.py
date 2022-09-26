import functools

import wrapt

from src.core.plateau.errors import AbroadPlateauException


def define_plateau(plateau, generator):
    """
    Retrieves first line of instructions (related to the plateau) from input file via gen
    :param plateau:
    :param generator:
    :return:
    """
    pl_x, pl_y = next(generator)
    plateau.x = pl_x
    plateau.y = pl_y

    return plateau


def check_plateau(plateau):
    """
    Decorator which checks that rover is inside plateau's area
    """

    @functools.wraps
    @wrapt.decorator
    def wrapper(func, instance, *args, **kwargs):
        x_coord, y_coord = func(*args, **kwargs)
        if not (x_coord <= plateau.x and y_coord <= plateau.y):
            raise AbroadPlateauException()

        return x_coord, y_coord

    return wrapper

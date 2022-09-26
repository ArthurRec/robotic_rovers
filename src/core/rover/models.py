import math
from dataclasses import dataclass

from logger import logger

from src.core.enums.direction import DirectionEnum
from src.core.plateau.errors import AbroadPlateauException
from src.core.plateau.models import Plateau
from src.core.plateau.plateau import check_plateau
from src.core.rover.rover import validate_instruction
from src.core.utils.constants import ROTATION_DEGREES_VALUE
from src.core.utils.descriptors import Direction, NonNegativeInt


# TODO: actually not a dataclass anymore
@dataclass
class Rover:
    """

    """
    instructions: str
    x: int = NonNegativeInt()
    y: int = NonNegativeInt()
    direction: Direction = DirectionEnum.N
    plateau: Plateau = None

    def left_rotation(self) -> Direction:
        """
        Rotates rover on the left
        :return: rovers direction
        """
        self.direction = DirectionEnum.E if (
                self.direction == DirectionEnum.S) else self.direction + ROTATION_DEGREES_VALUE

        return self.direction

    def right_rotation(self) -> Direction:
        """
        Rotates rover on the right
        :return: rovers direction
        """
        self.direction = DirectionEnum.S if (
                self.direction == DirectionEnum.E) else self.direction - ROTATION_DEGREES_VALUE

        return self.direction

    @check_plateau(plateau)
    def move_forward(self) -> tuple[int, int]:
        """
        Moves rover through axis x or axis y (by Bradis table)
        - for axis x we have: cos(degrees), where degrees can be 0 or 180
        - for axis y we have: sin(degrees), where degrees can be 90 or 270

        info about relation between DirectionEnum and degrees
        E = 0
        N = 90
        W = 180
        S = 270

        :return: rovers coords as a tuple: (x, y)
        """
        if self.direction in (DirectionEnum.E, DirectionEnum.W):
            self.x += int(math.cos(math.radians(self.direction)))
        else:
            self.y += int(math.sin(math.radians(self.direction)))

        return self.x, self.y

    def process_movements(self):
        """
        Goes through `instructions` and for each rover processes its movements
        """
        movements: dict = {
            "L": self.left_rotation,
            "R": self.right_rotation,
            "M": self.move_forward,
        }

        for char in self.instructions:
            if not validate_instruction(char):
                continue  # create specific exc
            else:
                try:
                    movements[char]()
                except AbroadPlateauException as exc:
                    logger.info(f"Rover exceeds limits of the plateau: {exc}")
                    raise AbroadPlateauException()

    def get_result(self) -> str:
        """
        Return final rover position on the plateau
        :return "1 3 N"
        """
        rover_movements: str = f"{self.x} {self.y} {DirectionEnum.backward_rel[self.direction]}"

        return rover_movements

    def run(self) -> str:
        """
        Acts as initial point of process start. Returns rover final data
        """
        self.process_movements()
        rover_data = self.get_result()

        return rover_data


def define_rover(generator, plateau) -> Rover:
    rover_x, rover_y, rover_dir, rover_ins = next(generator)

    rover: Rover = Rover(
        x=rover_x,
        y=rover_y,
        direction=rover_dir,
        instructions=rover_ins,
        plateau=plateau,
    )

    return rover

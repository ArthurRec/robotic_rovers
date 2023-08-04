from logger import logger

from src.core.plateau.models import Plateau
from src.core.plateau.plateau import define_plateau
from src.core.rover.models import define_rover
from src.core.utils.roverdata_reader import delegator, filereader_gen


def run_rovers(file_name: str) -> list[str]:
    """

    :param file_name:
    :return: list of rovers positions on the plateau after movements
    """
    # creating plateau with default coords
    plateau = Plateau(0, 0)  # 0, 0

    # initialize generators
    roverdata_gen = delegator(filereader_gen(file_name))
    _is_begin: bool = True
    rovers_results: list[str] = []
    _rovers_counter: int = 0

    while True:
        try:
            if not _is_begin:
                rover = define_rover(roverdata_gen, plateau)
            else:
                plateau = define_plateau(plateau, roverdata_gen)
                _is_begin: bool = False
                # once we set plateau data from the input file - move to the next cycle step
                continue

        except StopIteration as exc:
            # TODO: change logger output from f string to more lightweight way
            logger.info(
                f"Generator finished because it had retrieved all data from file: {exc}"
            )
            break

        else:
            rover_movements = rover.run()
            rovers_results.append(rover_movements)
            _rovers_counter += 1
            logger.info(f"Rover_{_rovers_counter} has been processed")

    return rovers_results

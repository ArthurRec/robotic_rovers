import collections

from src.core.enums.direction import DirectionEnum
from src.core.utils.constants import BULK_ROWS_NUM


def process_data(rover_pos: str, rover_ins: str) -> tuple:
    """
    Make some work with input sequence of chars / instructions by splitting them into parts
    :param rover_pos: 1 2 N
    :param rover_ins: LMLMLMLMM
    :return: split data
    """
    x, y, rover_dir = rover_pos.split(" ")
    rover_dir = DirectionEnum.relations[rover_dir]
    rover_ins = rover_ins.replace(" ", "")

    return int(x), int(y), rover_dir, rover_ins


# TODO: StopIteration
# read from file
def filereader_gen(file_name):
    """
    sub generator (called by main generator) to read the file
    """
    for row in open(file_name, "r"):
        # check that row is not an empty str
        if row:
            yield row


# translate data from other gen
# TODO: StopIteration
def delegator(gen):
    queue = collections.deque()

    # return first row of the data which should relates to plateau
    plateau_data = next(gen)
    pl_x, pl_y = plateau_data.strip().split()
    yield int(pl_x), int(pl_y)

    # TODO: check
    #   _str = yield from gen
    for _str in gen:
        if _str in ('\n', ""):
            continue
        else:
            _str: str = _str.strip('\n')
            queue.append(_str)
            if len(queue) == BULK_ROWS_NUM:
                rover_pos = queue.popleft()
                rover_instr = queue.popleft()

                yield process_data(rover_pos, rover_instr)
            else:
                continue

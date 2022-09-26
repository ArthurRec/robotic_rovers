import os
from pathlib import Path

# name of the readable file
DATA_FILENAME = "rovers_data.txt"

# for complete work of rover 2 rows of data needed
BULK_ROWS_NUM = 2

# amount of degrees on which rover rotates per one movement
ROTATION_DEGREES_VALUE = 90

# path to all data files
STORAGE_PATH = os.path.join(
    Path(os.path.dirname(__file__)).parent.parent.parent.absolute(), 'storage')

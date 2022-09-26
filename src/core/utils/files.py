import os

from src.core.utils.constants import STORAGE_PATH


def get_file_path(file_name: str) -> str:
    """
    Get full file path of the file with `file_name` inside the `storage` dir
    """
    file_path: str = os.path.join(STORAGE_PATH, file_name)
    is_correct: bool = os.path.exists(file_path) and os.path.isfile(file_path)

    if not is_correct:
        raise FileNotFoundError()

    return file_path

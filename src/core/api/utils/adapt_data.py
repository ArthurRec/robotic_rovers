def to_dict(data: list) -> dict:
    """
    Make dict from list of strings
    :param data:
    :return:
    """
    if isinstance(data, list):
        data_dict = dict()
        for idx, rover_pos in enumerate(data):
            rover_num: str = f"rover_{idx}"
            data_dict.update({rover_num: rover_pos})
    else:
        raise TypeError()

    return data_dict

import json

from logger import logger

from src.core.api.utils.adapt_data import to_dict
from src.core.api.utils.response import (
    SuccessResponse, InternalServerErrorResponse, api_respond)
from src.core.errors.direction import (
    NotValidDirectionError, DirectionTypeError)
from src.core.handlers.run_rovers import run_rovers
from src.core.plateau.errors import AbroadPlateauException
from src.core.utils.files import get_file_path


def get_rovers_movements(file_name: str) -> str:
    """
    API func
    Provides rovers final position on plateau after all movements provided by input file

    :param: file_name - is identifier of file in local folder with data files
    :return: str json data with rovers positions
    """
    try:
        file_path: str = get_file_path(file_name)

        # stars process of rovers movements to get their final positions on the plateau
        rovers_results: list[str] = run_rovers(file_path)

        # prepare result
        rovers_data: dict = to_dict(rovers_results)
        response = {
            'status_code': SuccessResponse().status_code.value,
            'body': {
                'rovers_positions': rovers_data
            },
        }
        logger.info(f'success response: {response}')

    except (
            FileNotFoundError, TypeError, json.JSONDecodeError, AttributeError, ValueError,
            NotValidDirectionError, DirectionTypeError, AbroadPlateauException
    ) as exc:
        logger.error(exc)
        response = {
            'status_code': InternalServerErrorResponse().status_code.value,
            'body': {
                'rovers_positions': {},
                'error_message': str(exc),
            }
        }

    return api_respond(
        body=response.get('body'),
        status=response.get('status_code'),
    )

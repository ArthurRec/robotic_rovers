import json
from dataclasses import dataclass
from http import HTTPStatus
from typing import Any


@dataclass
class Response(dict):
    status_code: int = None


@dataclass
class SuccessResponse(Response):
    status_code: int = HTTPStatus.OK


@dataclass
class InternalServerErrorResponse(Response):
    status_code: int = HTTPStatus.INTERNAL_SERVER_ERROR


def api_respond(body: Any, status: int = HTTPStatus.OK) -> str:
    """
    Create unified API respond
    """
    result_json = json.dumps(
        {
            "statusCode": status,
            "headers": {"Content-Type": "application/json"},
            "body": body,
        }
    )

    return result_json

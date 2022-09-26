from src.core.enums.rover_letters import RoverPossibleLettersEnum


def validate_instruction(ch: str) -> bool:
    return ch in RoverPossibleLettersEnum.values.keys()

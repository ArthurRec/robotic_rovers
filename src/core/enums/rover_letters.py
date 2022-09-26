class RoverPossibleLettersEnum:
    """
    The possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes the rover spin
    90 degrees left or right respectively, without moving from its current
    spot. 'M' means move forward one grid point, and maintain the same
    Heading.
    """
    L = "L"
    R = "R"
    M = "M"

    values = {
        'L': L,
        'R': R,
        'M': M,
    }

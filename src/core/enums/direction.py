class DirectionEnum:
    """
    Degrees related to the System of coordinates equal to
    globe directions
    """
    E = 0
    N = 90
    W = 180
    S = 270

    relations = {
        'E': E,
        'N': N,
        'W': W,
        'S': S,
    }

    backward_rel = {
        E: 'E',
        N: 'N',
        W: 'W',
        S: 'S',
    }

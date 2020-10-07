def ford_fulkerson(network: dict, source: str, sink: str) -> int:
    """
    The Ford-Fulkerson algorithm for maximum flow.

    >>> d = {'s': {'a': 9, 'b': 8, 'd': 5},
    ...      'a': {'c': 6, 't': 5},
    ...      'b': {'a': 3, 'c': 9, 'd': 4},
    ...      'c': {'t': 9},
    ...      'd': {'c': 4, 't': 7},
    ...      't': {}}

    >>> ford_fulkerson(d, 's', 't')
    21
    """
    pass


if __name__ == '__main__':
    import doctest

    doctest.testmod()

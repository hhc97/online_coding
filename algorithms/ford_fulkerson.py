def get_path(network: dict, source: str, sink: str, seen=None) -> list:
    """
    Returns a path with positive capacity from <source> to <sink>,
    or None if there is no such path.
    """
    if seen is None:
        seen = set()
    seen.add(source)

    to_visit = list(network[source].keys())
    for node in to_visit:
        if node not in seen:
            capacity = network[source][node]
            if capacity > 0:
                if node == sink:
                    return [[node, capacity]]
                path = get_path(network, node, sink, seen)
                if path:
                    return [[node, capacity]] + path
    return []


def invert_dict(network: dict) -> dict:
    """
    Inverts the network to create a residual graph.
    """
    inverted = {}
    for node, edges in network.items():
        for key in edges:
            if key not in inverted:
                inverted[key] = {}
            inverted[key][node] = 0
    return inverted


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

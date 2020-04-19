# https://open.kattis.com/problems/humancannonball


from math import sqrt


def _get_numbers():
    """
    Gets a line of input from stdin and return the numbers in a list.
    If there is only 1 number, return the number itself.
    """
    numbers = [float(v) for v in stdin.readline().split()]
    return numbers if len(numbers) > 1 else numbers[0]


def get_dist(a, b) -> float:
    """returns the distance between points a and b"""
    x1, y1 = a
    x2, y2 = b
    x_diff, y_diff = x1 - x2, y1 - y2
    return sqrt(x_diff ** 2 + y_diff ** 2)


def get_walk_time(a, b):
    return get_dist(a, b) / 5


def get_cannon_time(a, b):
    dist = get_dist(a, b)
    if dist >= 50:
        return (dist - 50) / 5 + 2
    else:
        return min(dist / 5, (50 - dist) / 5 + 2)


def make_adjacency_list():
    adj_lst = {}
    for i in range(num_cannons):
        for j in range(num_cannons):
            if i != j:
                adj_lst.setdefault(i + 1, []).append(
                    [get_cannon_time(cannons[i], cannons[j]), j + 1])
        adj_lst.setdefault(i + 1, []).append([get_cannon_time(cannons[i], destination), 'd'])
    for c in range(num_cannons):
        adj_lst.setdefault(0, []).append([get_walk_time(start, cannons[c]), c + 1])
    adj_lst.setdefault(0, []).append([get_walk_time(start, destination), 'd'])
    return adj_lst


if __name__ == '__main__':
    from sys import stdin

    start = _get_numbers()
    destination = _get_numbers()

    num_cannons = int(_get_numbers())
    cannons = []

    for _ in range(num_cannons):
        cannons.append(_get_numbers())

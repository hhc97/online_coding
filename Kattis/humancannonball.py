# https://open.kattis.com/problems/humancannonball


def _get_numbers():
    """
    Gets a line of input from stdin and return the numbers in a list.
    If there is only 1 number, return the number itself.
    """
    numbers = [float(v) for v in stdin.readline().split()]
    return numbers if len(numbers) > 1 else numbers[0]


if __name__ == '__main__':
    from sys import stdin

    start_x, start_y = _get_numbers()
    dest_x, dest_y = _get_numbers()

    num_cannons = int(_get_numbers())
    cannons = []

    for _ in range(num_cannons):
        cannons.append(_get_numbers())

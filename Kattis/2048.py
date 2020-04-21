# https://open.kattis.com/problems/2048


def _get_numbers():
    """
    Gets a line of input from stdin and return the numbers in a list.
    If there is only 1 number, return the number itself.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers if len(numbers) > 1 else numbers[0]


if __name__ == '__main__':
    from sys import stdin, stdout

    output = []
    grid = []

    for _ in range(4):
        grid.append(_get_numbers())

    move_direction = _get_numbers()

    stdout.write("\n".join(output))

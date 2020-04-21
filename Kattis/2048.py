# https://open.kattis.com/problems/2048


def _get_numbers():
    """
    Gets a line of input from stdin and return the numbers in a list.
    If there is only 1 number, return the number itself.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers if len(numbers) > 1 else numbers[0]


def _fill_left(orig: list):
    """Moves all numbers to their left if there is an empty space."""
    new_grid = []
    for row in orig:
        new_row = [n for n in row if n != 0]
        new_row += [0] * (4 - len(new_row))
        new_grid.append(new_row)
    return new_grid


def move_left(orig: list):
    """Moves the grid left, merging numbers when applicable."""
    orig = _fill_left(orig)
    for row in orig:
        for i in range(len(row) - 1):
            if row[i] == row[i + 1]:
                row[i] *= 2
                row[i + 1] = 0
                break
    return _fill_left(orig)


if __name__ == '__main__':
    from sys import stdin, stdout

    output = []
    grid = []

    for _ in range(4):
        grid.append(_get_numbers())

    move_direction = _get_numbers()

    stdout.write("\n".join(output))

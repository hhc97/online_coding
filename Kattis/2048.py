# https://open.kattis.com/problems/2048
# accepted answer, CPU time: 0.05s


"""
Sample input:
2 2 4 8
4 0 4 4
16 16 16 16
32 16 16 32
2

Sample output:
0 4 4 8
0 0 4 8
0 0 32 32
0 32 32 32

"""


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
    return _fill_left(orig)


def rotate_grid(orig: list, degree: int):
    """Returns a rotated grid by <degree> degrees clockwise"""
    if degree == 90:
        return [list(row) for row in zip(*orig[::-1])]
    elif degree == -90:
        return [list(row) for row in zip(*orig)][::-1]
    elif degree == 180 or degree == -180:
        return [row[::-1] for row in orig][::-1]


if __name__ == '__main__':
    from sys import stdin, stdout

    output = []
    grid = []

    for _ in range(4):
        grid.append(_get_numbers())

    move_direction = _get_numbers()

    # left
    if move_direction == 0:
        output = move_left(grid)

    # up
    elif move_direction == 1:
        rotated = rotate_grid(grid, -90)
        rotated = move_left(rotated)
        output = rotate_grid(rotated, 90)

    # right
    elif move_direction == 2:
        rotated = rotate_grid(grid, 180)
        rotated = move_left(rotated)
        output = rotate_grid(rotated, -180)

    # down
    elif move_direction == 3:
        rotated = rotate_grid(grid, 90)
        rotated = move_left(rotated)
        output = rotate_grid(rotated, -90)

    output = [[str(i) for i in row] for row in output]
    output = [' '.join(row) for row in output]
    stdout.write("\n".join(output))

# https://open.kattis.com/problems/10kindsofpeople


def _get_numbers():
    """
    Gets a line of input from stdin and return the numbers in a list.
    If there is only 1 number, return the number itself.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers if len(numbers) > 1 else numbers[0]


def _get_row():
    return [int(i) for i in stdin.readline().strip()]


def _get_map_copy():
    return [row[:] for row in original_map]


def _color(r, c, grid, original_color, color_value):
    if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
        if grid[r][c] != original_color or grid[r][c] == color_value:
            return
        if grid[r][c] == original_color:
            grid[r][c] = color_value
            _color(r - 1, c, grid, original_color, color_value)
            _color(r + 1, c, grid, original_color, color_value)
            _color(r, c - 1, grid, original_color, color_value)
            _color(r, c + 1, grid, original_color, color_value)


def is_connected(r1, c1, r2, c2):
    color_map = _get_map_copy()
    start_value = color_map[r1][c1]
    _color(r1, c1, color_map, start_value, 5)
    if color_map[r2][c2] == 5:
        if start_value == 0:
            return 'binary'
        else:
            return 'decimal'
    else:
        return 'neither'


if __name__ == '__main__':
    from sys import stdin, stdout

    output = []

    rows, cols = _get_numbers()
    original_map = []
    for _ in range(rows):
        original_map.append(_get_row())

    for _ in range(_get_numbers()):
        row1, col1, row2, col2 = _get_numbers()
        row1 -= 1
        col1 -= 1
        row2 -= 1
        col2 -= 1
        if original_map[row1][col1] != original_map[row2][col2]:
            output.append('neither')
        else:
            output.append(is_connected(row1, col1, row2, col2))

    stdout.write("\n".join(output))

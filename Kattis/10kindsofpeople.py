# https://open.kattis.com/problems/10kindsofpeople
# accepted answer, CPU time: 0.84s


def _get_numbers():
    """
    Gets a line of input from stdin and return the numbers in a list.
    If there is only 1 number, return the number itself.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers if len(numbers) > 1 else numbers[0]


def _get_row():
    return [int(v) for v in stdin.readline().strip()]


def _get_map_copy():
    return [row[:] for row in original_map]


def _color(r, c, grid, orig, color_value):
    row_limit = len(grid)
    col_limit = len(grid[0])
    q = [[r, c]]
    while q:
        row, col = q.pop()
        if 0 <= row < row_limit and 0 <= col < col_limit:
            color = grid[row][col]
            if color == orig:
                grid[row][col] = color_value
                q.extend([[row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]])


if __name__ == '__main__':
    from sys import stdin, stdout

    output = []

    rows, cols = _get_numbers()
    original_map = []
    for _ in range(rows):
        original_map.append(_get_row())

    color_map = _get_map_copy()
    current_color = 2
    for i in range(len(color_map)):
        for j in range(len(color_map[0])):
            if color_map[i][j] <= 1:
                _color(i, j, color_map, original_map[i][j], current_color)
                current_color += 1

    for _ in range(_get_numbers()):
        row1, col1, row2, col2 = _get_numbers()
        row1 -= 1
        col1 -= 1
        row2 -= 1
        col2 -= 1
        original_color = original_map[row1][col1]
        if color_map[row1][col1] == color_map[row2][col2]:
            if original_color == 1:
                output.append('decimal')
            else:
                output.append('binary')
        else:
            output.append('neither')

    stdout.write("\n".join(output))

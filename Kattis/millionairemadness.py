# https://open.kattis.com/problems/millionairemadness


def _get_numbers():
    """
    Gets a line of input from stdin and return the numbers in a list.
    If there is only 1 number, return the number itself.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers if len(numbers) > 1 else numbers[0]


def make_adjacency_list(grid):
    d = {}
    max_row, max_col = len(grid), len(grid[0])
    for i in range(max_row):
        for j in range(max_col):
            neighbors = []
            for i2 in range(i - 1, i + 2):
                for j2 in range(j - 1, j + 2):
                    if i2 != i or j2 != j:
                        if 0 <= i2 < max_row and 0 <= j2 < max_col:
                            if i2 == i:
                                neighbors.append(grid[i2][j2])
                            if j2 == j:
                                neighbors.append(grid[i2][j2])
            d[grid[i][j]] = neighbors
    return d


if __name__ == '__main__':
    from sys import stdin, stdout

    output = []
    bank_vault = []

    num_rows, num_cols = _get_numbers()
    for _ in range(num_rows):
        bank_vault.append(_get_numbers())

    stdout.write("\n".join(output))

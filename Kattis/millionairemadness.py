# https://open.kattis.com/problems/millionairemadness


from heapq import heapify, heappush, heappop


def _get_numbers():
    """
    Gets a line of input from stdin and return the numbers in a list.
    If there is only 1 number, return the number itself.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers if len(numbers) > 1 else numbers[0]


def get_min_ladder_height(grid: list, max_row: int, max_col: int) -> int:
    min_heap = [(0, 0, 0)]
    heapify(min_heap)
    min_ladder_height = 0
    visited = [[False for _ in range(max_col)] for _ in range(max_row)]

    while min_heap:
        ladder, row, col = heappop(min_heap)
        if ladder > min_ladder_height:
            min_ladder_height = ladder
        if row == max_row - 1 and col == max_col - 1:
            return min_ladder_height

        if visited[row][col]:
            continue
        visited[row][col] = True

        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        for i, j in neighbors:
            if 0 <= i < max_row and 0 <= j < max_col:
                if not visited[i][j]:
                    heappush(min_heap, (grid[i][j] - grid[row][col], i, j))


if __name__ == '__main__':
    from sys import stdin

    bank_vault = []

    num_rows, num_cols = _get_numbers()
    for _ in range(num_rows):
        bank_vault.append(_get_numbers())

    print(get_min_ladder_height(bank_vault, num_rows, num_cols))

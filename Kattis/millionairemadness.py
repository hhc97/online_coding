# https://open.kattis.com/problems/millionairemadness


from heapq import heapify, heappush, heappop


def _get_numbers():
    """
    Gets a line of input from stdin and return the numbers in a list.
    If there is only 1 number, return the number itself.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers if len(numbers) > 1 else numbers[0]


if __name__ == '__main__':
    from sys import stdin

    bank_vault = []

    num_rows, num_cols = _get_numbers()
    for _ in range(num_rows):
        bank_vault.append(_get_numbers())

    visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]

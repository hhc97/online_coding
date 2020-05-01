# https://open.kattis.com/problems/grassseed
# accepted answer, CPU time: 0.05s


"""
Sample input:
0.75
2
2 3.333
3.41 4.567

Sample output:
16.6796025

"""


def _get_numbers(first=False):
    """
    Gets a line of input from stdin and return the numbers in a list.
    If <first> is True, then return the first element of the list.
    """
    numbers = [float(v) for v in stdin.readline().split()]
    return numbers[0] if first else numbers


if __name__ == '__main__':
    from sys import stdin

    unit_cost = _get_numbers(True)
    n = int(_get_numbers(True))

    total_cost = 0
    for _ in range(n):
        x, y = _get_numbers()
        total_cost += x * y * unit_cost

    print(total_cost)

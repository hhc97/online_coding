# https://open.kattis.com/problems/pet
# accepted answer, CPU time: 0.05s


"""
Sample input:
4 4 3 3
5 4 3 5
5 5 2 4
5 5 5 1
4 4 4 4

Sample output:
2 17

"""


def _get_numbers(first=False):
    """
    Gets a line of input from stdin and return the numbers in a list.
    If <first> is True, then return the first element of the list.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers[0] if first else numbers


if __name__ == '__main__':
    from sys import stdin

    points = []
    for _ in range(5):
        points.append(sum(_get_numbers()))

    best = max(points)

    print(points.index(best) + 1, best)

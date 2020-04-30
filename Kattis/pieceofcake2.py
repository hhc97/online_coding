# https://open.kattis.com/problems/pieceofcake2
# accepted answer, CPU time: 0.05s


"""
Sample input:
10 4 7

Sample output:
168

"""


def _get_numbers(first=False):
    """
    Gets a line of input from stdin and return the numbers in a list.
    If there is only 1 number, return the number itself.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers[0] if first else numbers


if __name__ == '__main__':
    from sys import stdin

    side, x, y = _get_numbers()

    best_x = max(side - x, x)
    best_y = max(side - y, y)

    print(best_x * best_y * 4)

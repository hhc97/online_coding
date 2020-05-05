# https://open.kattis.com/problems/romans
# accepted answer, CPU time: 0.05s


"""
Sample input:
20.267

Sample output:
22046

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

    miles = _get_numbers(True)

    print(round(5280000 / 4854 * miles))

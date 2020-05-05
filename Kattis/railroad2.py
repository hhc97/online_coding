# https://open.kattis.com/problems/railroad2
# accepted answer, CPU time: 0.05s


"""
Sample input:
1 3

Sample output:
impossible

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

    a, b = _get_numbers()

    if b % 2 == 0:
        print('possible')
    else:
        print('impossible')

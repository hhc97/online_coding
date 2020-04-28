# https://open.kattis.com/problems/tarifa
# accepted answer, CPU time: 0.05s


"""
Sample input:
10
3
4
6
2

Sample output:
28

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

    monthly_limit = _get_numbers(True)
    months = _get_numbers(True)

    used = 0
    for i in range(months):
        used += _get_numbers(True)
    print(monthly_limit * (months + 1) - used)

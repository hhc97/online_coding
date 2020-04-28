# https://open.kattis.com/problems/transitwoes
# accepted answer, CPU time: 0.05s


"""
Sample input:
0 20 2
2 2 2
5 5
3 5

Sample output:
yes

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

    s, t, n = _get_numbers()
    walk_times = _get_numbers()
    bus_times = _get_numbers()
    bus_intervals = _get_numbers()

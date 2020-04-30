# https://open.kattis.com/problems/sibice
# accepted answer, CPU time: 0.05s


"""
Sample input:
5 3 4
3
4
5
6
7

Sample output:
DA
DA
DA
NE
NE

"""

from math import sqrt


def _get_numbers(first=False):
    """
    Gets a line of input from stdin and return the numbers in a list.
    If there is only 1 number, return the number itself.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers[0] if first else numbers


if __name__ == '__main__':
    from sys import stdin, stdout

    output = []

    n, w, h = _get_numbers()

    max_length = sqrt(w ** 2 + h ** 2)

    for _ in range(n):
        match_length = _get_numbers(True)
        if match_length <= max_length:
            output.append('DA')
        else:
            output.append('NE')

    stdout.write("\n".join(output))

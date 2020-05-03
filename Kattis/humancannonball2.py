# https://open.kattis.com/problems/humancannonball2
# accepted answer, CPU time: 0.05s


"""
Sample input:
11
19 45 20 9 12
20 45 20 9 12
25 45 20 9 12
20 43 20 9 12
20 47.5 20 9 12
20 45 17 9 12
20 45 24 9 12
20 45 20 10 12
20 45 20 9 11
20 45 20 9.0 11.5
20 45 18.1 9 12

Sample output:
Not Safe
Safe
Not Safe
Not Safe
Not Safe
Not Safe
Not Safe
Not Safe
Not Safe
Safe
Safe

"""

from math import cos, sin, pi


def _get_numbers(first=False):
    """
    Gets a line of input from stdin and return the numbers in a list.
    If <first> is True, then return the first element of the list.
    """
    numbers = [float(v) for v in stdin.readline().split()]
    return numbers[0] if first else numbers


def deg_to_radian(deg: float) -> float:
    return deg * (pi / 180)


def check_safe(lst: list) -> str:
    """Returns whether this launch makes it through safely."""
    v0, theta, x1, h1, h2 = lst

    theta = deg_to_radian(theta)

    cross_time = x1 / (v0 * cos(theta))

    y_at_cross = v0 * cross_time * sin(theta) - 0.5 * 9.81 * cross_time ** 2

    if h2 - y_at_cross >= 1 and y_at_cross - h1 >= 1:
        return 'Safe'
    return 'Not Safe'


if __name__ == '__main__':
    from sys import stdin, stdout

    output = []

    n = int(_get_numbers(True))

    for _ in range(n):
        output.append(check_safe(_get_numbers()))

    stdout.write("\n".join(output))

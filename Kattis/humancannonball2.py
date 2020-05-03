# https://open.kattis.com/problems/humancannonball2


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


def _get_numbers(first=False):
    """
    Gets a line of input from stdin and return the numbers in a list.
    If <first> is True, then return the first element of the list.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers[0] if first else numbers


if __name__ == '__main__':
    from sys import stdin, stdout

    output = []

    n = _get_numbers(True)

    for _ in range(n):
        pass

    stdout.write("\n".join(output))

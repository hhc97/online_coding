# https://open.kattis.com/problems/dicecup


"""
Sample input:
12 20

Sample output:
13
14
15
16
17
18
19
20
21

"""


def _get_numbers():
    """
    Gets a line of input from stdin and return the numbers in a list.
    If there is only 1 number, return the number itself.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers if len(numbers) > 1 else numbers[0]


if __name__ == '__main__':
    from sys import stdin, stdout

    output = []

    a, b = _get_numbers()

    stdout.write("\n".join(output))

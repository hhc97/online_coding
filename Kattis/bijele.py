# https://open.kattis.com/problems/bijele
# accepted answer, CPU time: 0.05s


"""
Sample input:
2 1 2 1 2 1

Sample output:
-1 0 0 1 0 7

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

    pieces = _get_numbers()
    correct = [1, 1, 2, 2, 2, 8]

    for curr, wanted in zip(pieces, correct):
        output.append(str(wanted - curr))

    stdout.write(" ".join(output))

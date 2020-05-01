# https://open.kattis.com/problems/filip
# accepted answer, CPU time: 0.05s


"""
Sample input:
839 237

Sample output:
938

"""


def _get_numbers(first=False):
    """
    Gets a line of input from stdin and return the numbers in a list.
    If <first> is True, then return the first element of the list.
    """
    numbers = [int(v) for v in stdin.readline()[::-1].split()]
    return numbers[0] if first else numbers


if __name__ == '__main__':
    from sys import stdin

    a, b = _get_numbers()

    if a > b:
        print(a)
    else:
        print(b)

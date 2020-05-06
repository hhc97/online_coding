# https://open.kattis.com/problems/PROBLEM_ID
# accepted answer, CPU time: 0.05s


"""
Sample input:

Sample output:

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

    a, b = _get_numbers()

    stdout.write("\n".join(output))

# https://open.kattis.com/problems/PROBLEM_ID


def _get_numbers() -> list:
    """
    Gets a line of input from stdin and returns a list
    of it's individual ints.
    """
    return [int(v) for v in stdin.readline().split()]


if __name__ == '__main__':
    from sys import stdin, stdout

    output = []

    a, b = _get_numbers()

    stdout.write("\n".join(output))

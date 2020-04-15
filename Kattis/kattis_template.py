# https://open.kattis.com/problems/PROBLEM_ID


def _get_numbers() -> list:
    """
    Gets a line of input from stdin and returns a list
    of it's individual ints.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers if len(numbers) > 1 else numbers[0]


if __name__ == '__main__':
    from sys import stdin, stdout

    output = []

    a, b = _get_numbers()

    stdout.write("\n".join(output))

# https://open.kattis.com/problems/oddities
# accepted answer, CPU time: 0.05s


"""
Sample input:
3
10
9
-5

Sample output:
10 is even
9 is odd
-5 is odd

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
        number = _get_numbers(True)
        if number % 2 == 0:
            output.append(f'{number} is even')
        else:
            output.append(f'{number} is odd')

    stdout.write("\n".join(output))

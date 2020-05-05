# https://open.kattis.com/problems/quickestimate
# accepted answer, CPU time: 0.05s


"""
Sample input:
3
0
10
100

Sample output:
1
2
3

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
        est = stdin.readline().strip()
        output.append(str(len(est)))

    stdout.write("\n".join(output))

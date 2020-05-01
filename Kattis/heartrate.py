# https://open.kattis.com/problems/heartrate
# accepted answer, CPU time: 0.06s


"""
Sample input:
2
6 5.0000
2 3.1222

Sample output:
60.0000 72.0000 84.0000
19.2172 38.4344 57.6517

"""


def _get_numbers(first=False):
    """
    Gets a line of input from stdin and return the numbers in a list.
    If <first> is True, then return the first element of the list.
    """
    numbers = [float(v) for v in stdin.readline().split()]
    return numbers[0] if first else numbers


if __name__ == '__main__':
    from sys import stdin, stdout

    output = []

    n = int(_get_numbers(True))

    for _ in range(n):
        b, p = _get_numbers()
        BPM = (60 * b) / p
        var = 60 / p
        output.append(f'{BPM - var} {BPM} {BPM + var}')

    stdout.write("\n".join(output))

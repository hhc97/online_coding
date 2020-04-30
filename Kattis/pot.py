# https://open.kattis.com/problems/pot
# accepted answer, CPU time: 0.05s


"""
Sample input:
2
212
1253

Sample output:
1953566

"""


def _get_numbers(first=False):
    """
    Gets a line of input from stdin and return the numbers in a list.
    If there is only 1 number, return the number itself.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers[0] if first else numbers


if __name__ == '__main__':
    from sys import stdin

    n = _get_numbers(True)

    total = 0
    for _ in range(n):
        num = str(_get_numbers(True))
        base = int(num[:-1])
        pwr = int(num[-1])
        total += base ** pwr
    print(total)

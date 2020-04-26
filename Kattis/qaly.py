# https://open.kattis.com/problems/qaly
# accepted answer, CPU time: 0.05s


"""
Sample input:
5
1.0 12.0
0.7 5.2
0.9 10.7
0.5 20.4
0.2 30.0

Sample output:
41.470

"""


def _get_numbers():
    """
    Gets a line of input from stdin and return the numbers in a list.
    If there is only 1 number, return the number itself.
    """
    numbers = [float(v) for v in stdin.readline().split()]
    return numbers if len(numbers) > 1 else numbers[0]


if __name__ == '__main__':
    from sys import stdin

    n = int(_get_numbers())

    total = 0
    for _ in range(n):
        a, b = _get_numbers()
        total += a * b

    print(total)

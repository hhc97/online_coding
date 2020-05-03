# https://open.kattis.com/problems/zamka
# accepted answer, CPU time: 0.07s


"""
Sample input:
100
500
12

Sample output:
129
480

"""


def _get_numbers(first=False):
    """
    Gets a line of input from stdin and return the numbers in a list.
    If <first> is True, then return the first element of the list.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers[0] if first else numbers


def sum_digits(num: int) -> int:
    return sum(int(s) for s in str(num))


if __name__ == '__main__':
    from sys import stdin

    L = _get_numbers(True)
    D = _get_numbers(True)
    X = _get_numbers(True)

    low, high = 0, 0
    for i in range(L, D + 1):
        if sum_digits(i) == X:
            low = i
            break

    for i in range(D, L - 1, -1):
        if sum_digits(i) == X:
            high = i
            break

    print(low)
    print(high)

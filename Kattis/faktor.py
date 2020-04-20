# https://open.kattis.com/problems/faktor
# accepted answer, CPU time: 0.05s


def _get_numbers():
    """
    Gets a line of input from stdin and return the numbers in a list.
    If there is only 1 number, return the number itself.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers if len(numbers) > 1 else numbers[0]


if __name__ == '__main__':
    from sys import stdin

    a, b = _get_numbers()

    if a == 1:
        print(b)
    else:
        print(a * (b - 1) + 1)

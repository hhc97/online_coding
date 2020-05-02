# https://open.kattis.com/problems/cetvrta
# accepted answer, CPU time: 0.05s


"""
Sample input:
5 5
5 7
7 5

Sample output:
7 7

"""


def _get_numbers(first=False):
    """
    Gets a line of input from stdin and return the numbers in a list.
    If <first> is True, then return the first element of the list.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers[0] if first else numbers


if __name__ == '__main__':
    from sys import stdin

    x_values = {}
    y_values = {}

    for _ in range(3):
        x, y = _get_numbers()
        if x in x_values:
            x_values[x] += 1
        else:
            x_values[x] = 1
        if y in y_values:
            y_values[y] += 1
        else:
            y_values[y] = 1

    for key in x_values:
        if x_values[key] == 1:
            print(key, end=' ')
    for key in y_values:
        if y_values[key] == 1:
            print(key)

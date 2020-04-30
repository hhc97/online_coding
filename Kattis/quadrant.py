# https://open.kattis.com/problems/quadrant
# accepted answer, CPU time: 0.05s


"""
Sample input:
9
-13

Sample output:
4

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

    x = _get_numbers(True)
    y = _get_numbers(True)

    if x > 0 and y > 0:
        print(1)
    elif y < 0 < x:
        print(4)
    elif x < 0 and y < 0:
        print(3)
    else:
        print(2)

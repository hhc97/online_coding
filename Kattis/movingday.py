# https://open.kattis.com/problems/movingday
# accepted answer, CPU time: 0.05s


"""
Sample input:
4 980
10 10 10
10 5 2
5 3 2
90 5 2

Sample output:
20

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

    boxes, vol = _get_numbers()

    largest = 0
    for _ in range(boxes):
        h, w, d = _get_numbers()
        volume = h * w * d
        if volume > largest:
            largest = volume

    print(largest - vol)

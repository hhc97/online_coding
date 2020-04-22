# https://open.kattis.com/problems/srednji


"""
Sample input:
7 4
5 7 2 4 3 1 6

Sample output:
4

"""


def _get_numbers():
    """
    Gets a line of input from stdin and return the numbers in a list.
    If there is only 1 number, return the number itself.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers if len(numbers) > 1 else numbers[0]


def median(lst: list) -> int:
    """
    Returns the median of the lst if the length is odd, else return 0.
    For len(lst) < 100000, using sorted() is faster than quickselect.
    """
    if len(lst) % 2 == 0:
        return 0
    return sorted(lst)[len(lst) // 2]


if __name__ == '__main__':
    from sys import stdin

    n, b = _get_numbers()
    number_lst = _get_numbers()

    curr_median = median(number_lst)

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


seen = set()


def get_num_medians(lst, wanted):
    total = 0
    curr_median = median(lst)
    if curr_median == wanted:
        if lst not in seen:
            seen.add(lst)
            total += 1
        else:
            return 0
    if len(lst) == 1:
        return total
    total += get_num_medians(lst[:-2], wanted)
    total += get_num_medians(lst[2:], wanted)
    total += get_num_medians(lst[1:-1], wanted)
    return total


if __name__ == '__main__':
    from sys import stdin

    n, b = _get_numbers()
    number_lst = tuple(_get_numbers())

    if len(number_lst) % 2 == 1:
        print(get_num_medians(number_lst, b))
    else:
        print(get_num_medians(number_lst[1:], b) + get_num_medians(number_lst[:-1], b))

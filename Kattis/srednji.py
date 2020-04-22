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


def get_median_index(lst, median):
    for i in range(len(lst)):
        if lst[i] == median:
            return i


def modify_list(lst, median):
    for i in range(len(lst)):
        value = lst[i]
        if value < median:
            lst[i] = -1
        elif value > median:
            lst[i] = 1
        else:
            lst[i] = 0


def _check_odd(start_index, end_index):
    return ((end_index + 1) - start_index) % 2 == 1


def count_sublists(lst):
    seen = {}
    running_sum = 0
    total = 0

    for i in range(len(lst)):
        running_sum += lst[i]

        if running_sum == 0:
            total += _check_odd(0, i)

        all_previous = []
        if running_sum in seen:
            all_previous = seen[running_sum]
            for index in all_previous:
                total += _check_odd(index + 1, i)

        all_previous.append(i)
        seen[running_sum] = all_previous
    return total


if __name__ == '__main__':
    from sys import stdin

    n, b = _get_numbers()
    number_lst = _get_numbers()

    modify_list(number_lst, b)
    print(count_sublists(number_lst))

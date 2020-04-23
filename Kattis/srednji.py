# https://open.kattis.com/problems/srednji
# accepted answer, CPU time: 0.10s


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


def find_median_index(lst, median):
    for i in range(len(lst)):
        if lst[i] == median:
            return i


def count_sublists(lst, median):
    median_index = find_median_index(lst, median)
    d = dict()
    d[0] = 1
    total = 0
    for i in range(median_index + 1, len(lst)):
        if lst[i] > median:
            total += 1
        else:
            total -= 1
        if total in d:
            d[total] += 1
        else:
            d[total] = 1

    answer = d[0]
    total = 0
    for i in range(median_index - 1, -1, -1):
        if lst[i] > median:
            total += 1
        else:
            total -= 1
        answer += d.setdefault(-total, 0)
    return answer


if __name__ == '__main__':
    from sys import stdin

    n, b = _get_numbers()
    number_lst = _get_numbers()

    print(count_sublists(number_lst, b))

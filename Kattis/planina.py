# https://open.kattis.com/problems/planina
# accepted answer, CPU time: 0.05s


"""
Sample input:
5

Sample output:
1089

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

    n = _get_numbers(True)
    single_line = 2
    for _ in range(n):
        single_line = 2 * single_line - 1
    print(single_line ** 2)

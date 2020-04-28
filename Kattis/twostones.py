# https://open.kattis.com/problems/twostones
# accepted answer, CPU time: 0.05s


"""
Sample input:
5

Sample output:
Alice

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

    stone_no = _get_numbers(True)

    if stone_no % 2 == 1:
        print('Alice')
    else:
        print('Bob')

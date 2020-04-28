# https://open.kattis.com/problems/carrots
# accepted answer, CPU time: 0.05s


"""
Sample input:
2 1
carrots?
bunnies

Sample output:
1

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

    contestants, carrots = _get_numbers()

    print(carrots)

# https://open.kattis.com/problems/bela
# accepted answer, CPU time: 0.05s


"""
Sample input:
4 H
AH
KH
QH
JH
TH
9H
8H
7H
AS
KS
QS
JS
TS
9S
8S
7S

Sample output:
92

"""


def _get_numbers(first=False):
    """
    Gets a line of input from stdin and return the numbers in a list.
    If <first> is True, then return the first element of the list.
    """
    numbers = stdin.readline().split()
    return numbers[0] if first else numbers


if __name__ == '__main__':
    from sys import stdin

    hands, trump = _get_numbers()
    hands = int(hands)

    scores = {'A': [11, 11], 'K': [4, 4], 'Q': [3, 3], 'J': [20, 2],
              'T': [10, 10], '9': [14, 0], '8': [0, 0], '7': [0, 0]}

    total_score = 0

    for _ in range(4 * hands):
        number, suit = list(stdin.readline().strip())
        if suit == trump:
            total_score += scores[number][0]
        else:
            total_score += scores[number][1]

    print(total_score)

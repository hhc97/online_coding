# https://open.kattis.com/problems/stararrangements
# accepted answer, CPU time: 0.05s


"""
Sample input:
50

Sample output:
50:
2,1
2,2
3,2
5,4
5,5
6,5
10,10
13,12
17,16
25,25

"""


def _get_numbers(first=False):
    """
    Gets a line of input from stdin and return the numbers in a list.
    If <first> is True, then return the first element of the list.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers[0] if first else numbers


if __name__ == '__main__':
    from sys import stdin, stdout

    num_stars = _get_numbers(True)

    output = [f'{num_stars}:']

    for i in range(2, num_stars // 2 + 2):
        two_rows = i * 2 - 1
        if num_stars % two_rows == 0 or num_stars % two_rows == i:
            output.append(f'{i},{i - 1}')

        if num_stars % i == 0:
            output.append(f'{i},{i}')

    stdout.write("\n".join(output))

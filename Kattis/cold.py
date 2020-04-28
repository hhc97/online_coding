# https://open.kattis.com/problems/cold
# accepted answer, CPU time: 0.05s


"""
Sample input:
3
5 -10 15

Sample output:
1

"""


def _get_numbers():
    """
    Gets a line of input from stdin and return the numbers in a list.
    If there is only 1 number, return the number itself.
    """
    return [int(v) for v in stdin.readline().split()]


if __name__ == '__main__':
    from sys import stdin

    stdin.readline()
    count = 0
    temps = _get_numbers()
    for t in temps:
        if t < 0:
            count += 1
    print(count)

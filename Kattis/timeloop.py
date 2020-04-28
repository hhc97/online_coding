# https://open.kattis.com/problems/timeloop
# accepted answer, CPU time: 0.05s


"""
Sample input:
5

Sample output:
1 Abracadabra
2 Abracadabra
3 Abracadabra
4 Abracadabra
5 Abracadabra

"""


def _get_numbers(first=False):
    """
    Gets a line of input from stdin and return the numbers in a list.
    If there is only 1 number, return the number itself.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers[0] if first else numbers


if __name__ == '__main__':
    from sys import stdin, stdout

    output = []

    num_loop = _get_numbers(True)

    for i in range(1, num_loop + 1):
        output.append(f'{i} Abracadabra')

    stdout.write("\n".join(output))

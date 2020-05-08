# https://open.kattis.com/problems/princesspeach
# accepted answer, CPU time: 0.05s


"""
Sample input:
20 4
5
10
12
16

Sample output:
0
1
2
3
4
6
7
8
9
11
13
14
15
17
18
19
Mario got 4 of the dangerous obstacles.

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

    output = []

    num_obstacles, num_found = _get_numbers()

    found = set()
    for _ in range(num_found):
        found.add(str(_get_numbers(True)))

    for i in range(num_obstacles):
        s = str(i)
        if s not in found:
            output.append(s)

    output.append(f'Mario got {len(found)} of the dangerous obstacles.')

    stdout.write("\n".join(output))

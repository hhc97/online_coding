# https://open.kattis.com/problems/collatz
# accepted answer, CPU time: 0.09s


"""
Sample input:
7 8
27 30
0 0

Sample output:
7 needs 13 steps, 8 needs 0 steps, they meet at 8
27 needs 95 steps, 30 needs 2 steps, they meet at 46

"""


def _get_numbers(first=False):
    """
    Gets a line of input from stdin and return the numbers in a list.
    If <first> is True, then return the first element of the list.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers[0] if first else numbers


def collatz(num: int) -> list:
    """
    Returns the collatz values of a number up until 1.
    """
    values = [num]
    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        values.append(num)
    return values


def get_meeting(lst1: list, lst2: list) -> tuple:
    """
    Returns the number and positions at which the two lists first meet.
    """
    num = 1
    for i, j in zip(lst1[::-1], lst2[::-1]):
        if i == j:
            num = i
            continue
        break
    return num, lst1.index(num), lst2.index(num)


if __name__ == '__main__':
    from sys import stdin, stdout

    output = []

    a, b = _get_numbers()
    while a and b:
        meeting_num, meeting_a, meeting_b = get_meeting(collatz(a), collatz(b))
        output.append(f'{a} needs {meeting_a} steps, {b} needs {meeting_b} steps, they meet at {meeting_num}')
        a, b = _get_numbers()

    stdout.write("\n".join(output))

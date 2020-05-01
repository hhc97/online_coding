# https://open.kattis.com/problems/hangingout
# accepted answer, CPU time: 0.05s


"""
Sample input:
4 5
enter 3
enter 2
leave 1
enter 1
enter 2

Sample output:
2

"""


def _get_numbers(first=False):
    """
    Gets a line of input from stdin and return the numbers in a list.
    If <first> is True, then return the first element of the list.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers[0] if first else numbers


if __name__ == '__main__':
    from sys import stdin

    capacity, n = _get_numbers()

    curr_capacity = 0
    no_rejected = 0
    for _ in range(n):
        indicator, number = stdin.readline().split()
        number = int(number)
        if indicator == 'enter':
            if curr_capacity + number > capacity:
                no_rejected += 1
            else:
                curr_capacity += number
        else:
            curr_capacity -= number
    print(no_rejected)

# https://open.kattis.com/problems/sumsquareddigits
# accepted answer, CPU time: 0.07s


"""
Sample input:
3
1 10 1234
2 3 98765
3 16 987654321

Sample output:
1 30
2 19
3 696

"""


def _get_numbers(first=False):
    """
    Gets a line of input from stdin and return the numbers in a list.
    If <first> is True, then return the first element of the list.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers[0] if first else numbers


def get_base_values(number: int, base_val: int) -> list:
    """Returns the base values of number written in base <base>"""
    values = []
    while number > 0:
        values.append(number % base_val)
        number //= base_val
    return values


if __name__ == '__main__':
    from sys import stdin, stdout

    output = []

    n = _get_numbers(True)

    for _ in range(n):
        test_no, base, num = _get_numbers()
        total = sum(i ** 2 for i in get_base_values(num, base))
        output.append(f'{test_no} {total}')

    stdout.write("\n".join(output))

# https://open.kattis.com/problems/luhnchecksum
# accepted answer, CPU time: 0.07s


"""
Sample input:
3
00554
999
1234567890123411

Sample output:
PASS
FAIL
PASS

"""


def _get_numbers(first=False):
    """
    Gets a line of input from stdin and return the numbers in a list.
    If <first> is True, then return the first element of the list.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers[0] if first else numbers


def luhn_checksum(num: list) -> bool:
    """
    Performs the luhn checksum on the list representing an integer.
    """

    def _mul(number: int) -> int:
        number *= 2
        return sum(int(s) for s in str(number))

    for i in range(len(num) - 2, -1, -2):
        num[i] = _mul(num[i])
    return sum(num) % 10 == 0


if __name__ == '__main__':
    from sys import stdin, stdout

    output = []

    n = _get_numbers(True)

    for _ in range(n):
        if luhn_checksum(list(int(i) for i in stdin.readline().strip())):
            output.append('PASS')
        else:
            output.append('FAIL')

    stdout.write("\n".join(output))

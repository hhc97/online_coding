# https://open.kattis.com/problems/nastyhacks
# accepted answer, CPU time: 0.05s


"""
Sample input:
3
0 100 70
100 130 30
-100 -70 40

Sample output:
advertise
does not matter
do not advertise

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

    n = _get_numbers(True)

    for _ in range(n):
        no_ad, ad, ad_cost = _get_numbers()
        net = ad - ad_cost
        if net < no_ad:
            output.append('do not advertise')
        elif net > no_ad:
            output.append('advertise')
        else:
            output.append('does not matter')

    stdout.write("\n".join(output))

# https://open.kattis.com/problems/polymul1


"""
Sample input:
2
2
1 0 5
1
0 -2
4
1 1 -1 1 1
4
9 -8 7 6 5

Sample output:
3
0 -2 0 -10
8
9 1 -10 30 5 -2 8 11 5

"""


def _get_numbers():
    """
    Gets a line of input from stdin and return the numbers in a list.
    If there is only 1 number, return the number itself.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers if len(numbers) > 1 else numbers[0]


if __name__ == '__main__':
    from sys import stdin, stdout

    output = []

    num_test_cases = _get_numbers()

    for _ in range(num_test_cases):
        degree_a = _get_numbers()
        poly_a = _get_numbers()
        degree_b = _get_numbers()
        poly_b = _get_numbers()
        print(degree_a, degree_b, poly_a, poly_b)

    stdout.write("\n".join(output))

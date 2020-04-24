# https://open.kattis.com/problems/polymul1
# accepted answer, CPU time: 0.13s


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


def multiply(x, y):
    """
    <a> and <b> are provided in the form [degree, value].
    Returns the value of the product of a and b.
    """
    deg_a, val_a = x
    deg_b, val_b = y
    return [deg_a + deg_b, val_a * val_b]


if __name__ == '__main__':
    from sys import stdin, stdout

    output = []

    num_test_cases = _get_numbers()

    for _ in range(num_test_cases):
        degree_a = _get_numbers()
        poly_a = _get_numbers()
        degree_b = _get_numbers()
        poly_b = _get_numbers()

        result = {}
        result_degree = 0
        for a in range(degree_a + 1):
            for b in range(degree_b + 1):
                coeff_a = poly_a[a]
                coeff_b = poly_b[b]
                product_degree, product_coeff = multiply([a, coeff_a], [b, coeff_b])
                if product_degree > result_degree:
                    result_degree = product_degree
                if product_degree in result:
                    result[product_degree] += product_coeff
                else:
                    result[product_degree] = product_coeff
        output.append(str(result_degree))
        string_out = []
        for deg in range(result_degree + 1):
            string_out.append(str(result.setdefault(deg, 0)))
        output.append(' '.join(string_out))

    stdout.write("\n".join(output))

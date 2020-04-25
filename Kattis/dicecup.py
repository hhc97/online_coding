# https://open.kattis.com/problems/dicecup
# accepted answer, CPU time: 0.05s


"""
Sample input:
12 20

Sample output:
13
14
15
16
17
18
19
20
21

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
    probabilities = {}

    a, b = _get_numbers()
    p_a, p_b = 1 / a, 1 / b

    for i in range(1, a + 1):
        for j in range(1, b + 1):
            outcome = i + j
            p_outcome = p_a * p_b
            if outcome in probabilities:
                probabilities[outcome] += p_outcome
            else:
                probabilities[outcome] = p_outcome

    p_max = max(probabilities.values())
    for value, p in probabilities.items():
        if p == p_max:
            output.append(value)

    output.sort()
    output = [str(v) for v in output]
    stdout.write("\n".join(output))

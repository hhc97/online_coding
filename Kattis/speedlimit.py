# https://open.kattis.com/problems/speedlimit
# accepted answer, CPU time: 0.05s


"""
Sample input:
3
20 2
30 6
10 7
2
60 1
30 5
4
15 1
25 2
30 3
10 5
-1

Sample output:
170 miles
180 miles
90 miles

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

    while True:
        n = _get_numbers(True)
        if n == -1:
            break
        segment_total = 0
        prev_time = 0
        for _ in range(n):
            speed, time = _get_numbers()
            segment_total += speed * (time - prev_time)
            prev_time = time
        output.append(f'{segment_total} miles')

    stdout.write("\n".join(output))

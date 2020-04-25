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

if __name__ == '__main__':
    from sys import stdin, stdout

    output = []

    first = stdin.readline().split()
    a, b = int(first[0]), int(first[1])
    if a > b:
        high = a
        low = b
    else:
        low = a
        high = b
    for i in range(low + 1, high + 2):
        output.append(str(i))

    stdout.write("\n".join(output))

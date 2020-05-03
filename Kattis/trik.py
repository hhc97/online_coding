# https://open.kattis.com/problems/trik
# accepted answer, CPU time: 0.05s


"""
Sample input:
CBABCACCC

Sample output:
1

"""

if __name__ == '__main__':
    from sys import stdin

    sequence = stdin.readline().strip()

    curr = 1

    for move in sequence:
        if curr == 1:
            if move == 'A':
                curr = 2
            elif move == 'C':
                curr = 3
        elif curr == 2:
            if move == 'A':
                curr = 1
            elif move == 'B':
                curr = 3
        elif curr == 3:
            if move == 'B':
                curr = 2
            elif move == 'C':
                curr = 1
    print(curr)

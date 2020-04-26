# https://open.kattis.com/problems/autori
# accepted answer, CPU time: 0.05s


"""
Sample input:
Knuth-Morris-Pratt

Sample output:
KMP

"""

if __name__ == '__main__':
    from sys import stdin

    name = stdin.readline().split('-')
    shortened = []
    for n in name:
        shortened.append(n[0])
    print(''.join(shortened))

# https://open.kattis.com/problems/conundrum
# accepted answer, CPU time: 0.05s


"""
Sample input:
SECRET

Sample output:
4

"""

if __name__ == '__main__':
    from sys import stdin

    cipher = stdin.readline().strip()

    length = len(cipher)

    wanted = ['P', 'E', 'R']

    need_changed = 0

    for i in range(0, length, 3):
        for cip_letter, wanted_letter in zip(cipher[i: i + 3], wanted):
            if cip_letter != wanted_letter:
                need_changed += 1

    print(need_changed)

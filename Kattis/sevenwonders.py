# https://open.kattis.com/problems/sevenwonders
# accepted answer, CPU time: 0.06s


"""
Sample input:
TTCCGG

Sample output:
26

"""

if __name__ == '__main__':
    from sys import stdin

    sequence = stdin.readline().strip()

    totals = {'T': 0, 'C': 0, 'G': 0}

    score = 0
    for letter in sequence:
        totals[letter] += 1

    score += min(totals.values()) * 7
    for times_played in totals.values():
        score += times_played ** 2

    print(score)

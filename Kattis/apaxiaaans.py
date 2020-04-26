# https://open.kattis.com/problems/apaxiaaans
# accepted answer, CPU time: 0.05s


"""
Sample input:
roooooobertapalaxxxxios

Sample output:
robertapalaxios

"""

if __name__ == '__main__':
    from sys import stdin

    name = stdin.readline().strip()
    letters = [name[0]]
    curr = letters[0]
    for let in name:
        if let != curr:
            letters.append(let)
        curr = let
    print(''.join(letters))

# https://open.kattis.com/problems/avion
# accepted answer, CPU time: 0.05s


"""
Sample input:
47-FBI
BOND-007
RF-FBI18
MARICA-13
13A-FBILL

Sample output:
1 3 5

"""

if __name__ == '__main__':
    from sys import stdin, stdout

    number = 1
    output = []
    curr = stdin.readline().strip()
    while curr:
        if 'FBI' in curr:
            output.append(str(number))
        number += 1
        curr = stdin.readline().strip()

    if output:
        stdout.write(' '.join(output))
    else:
        print('HE GOT AWAY!')

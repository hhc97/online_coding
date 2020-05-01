# https://open.kattis.com/problems/hissingmicrophone
# accepted answer, CPU time: 0.05s


"""
Sample input:
amiss

Sample output:
hiss

"""

if __name__ == '__main__':
    from sys import stdin

    string = stdin.readline().strip()
    if 'ss' in string:
        print('hiss')
    else:
        print('no hiss')

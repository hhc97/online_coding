# https://open.kattis.com/problems/nodup
# accepted answer, CPU time: 0.05s


"""
Sample input:
IN THE RAIN AND THE SNOW

Sample output:
no

"""

if __name__ == '__main__':
    from sys import stdin

    words = stdin.readline().split()
    if len(words) == len(set(words)):
        print('yes')
    else:
        print('no')

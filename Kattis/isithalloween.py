# https://open.kattis.com/problems/isithalloween
# accepted answer, CPU time: 0.05s


"""
Sample input:
OCT 31

Sample output:
yup

"""

if __name__ == '__main__':
    from sys import stdin

    day = stdin.readline().strip()
    if day == 'DEC 25' or day == 'OCT 31':
        print('yup')
    else:
        print('nope')

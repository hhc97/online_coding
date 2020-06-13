# https://open.kattis.com/problems/heliocentric
# accepted answer, CPU time: 0.06s


"""
Sample input:
0 0
364 686
360 682
0 1
1 0

Sample output:
Case 1: 0
Case 2: 1
Case 3: 5
Case 4: 239075
Case 5: 11679

"""


def get_sync(a: int, b: int) -> int:
    count = 0
    while a != 0 or b != 0:
        a += 1
        b += 1
        a = a % 365
        b = b % 687
        count += 1
    return count


if __name__ == '__main__':
    from sys import stdin, stdout

    # earth: 365
    # mars: 687
    output = []

    testcase = stdin.readline().strip()

    case_no = 1
    while testcase:
        earth, mars = [int(i) for i in testcase.split()]
        output.append(f'Case {case_no}: {get_sync(earth, mars)}')

        testcase = stdin.readline().strip()
        case_no += 1

    stdout.write("\n".join(output))

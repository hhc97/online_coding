# https://open.kattis.com/problems/fizzbuzz
# accepted answer, CPU time: 0.05s


"""
Sample input:
2 3 7

Sample output:
1
Fizz
Buzz
Fizz
5
FizzBuzz
7

"""

if __name__ == '__main__':
    from sys import stdin, stdout

    first = stdin.readline().split()
    fizz, buzz, n = int(first[0]), int(first[1]), int(first[2])
    output = []
    for i in range(1, n + 1):
        is_fizz = i % fizz == 0
        is_buzz = i % buzz == 0
        if is_fizz and is_buzz:
            output.append('FizzBuzz')
            continue
        elif is_fizz:
            output.append('Fizz')
        elif is_buzz:
            output.append('Buzz')
        else:
            output.append(str(i))
    stdout.write('\n'.join(output))

# https://open.kattis.com/problems/spavanac
# accepted answer, CPU time: 0.05s


"""
Sample input:
0 30

Sample output:
23 45

"""


def _get_numbers(first=False):
    """
    Gets a line of input from stdin and return the numbers in a list.
    If <first> is True, then return the first element of the list.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers[0] if first else numbers


def convert_time(hours: int, minutes: int) -> list:
    """
    Takes in a 24 hour format time and returns a
    24 hour format time 45 mins earlier.
    """
    if minutes >= 45:
        minutes -= 45
    else:
        minutes += 15
        if hours == 0:
            hours = 23
        else:
            hours -= 1
    return [hours, minutes]


if __name__ == '__main__':
    from sys import stdin

    hour, minute = _get_numbers()
    hour, minute = convert_time(hour, minute)
    print(hour, minute)

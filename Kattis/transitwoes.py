# https://open.kattis.com/problems/transitwoes
# accepted answer, CPU time: 0.05s


"""
Sample input:
0 20 2
2 2 2
5 5
3 5

Sample output:
yes

"""


def _get_numbers(first=False):
    """
    Gets a line of input from stdin and return the numbers in a list.
    If there is only 1 number, return the number itself.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers[0] if first else numbers


def get_bus_wait(elapsed: int, bus_interval: int) -> int:
    """Returns the amount of time to wait until the next bus arrives."""
    if elapsed % bus_interval == 0:
        return 0
    if elapsed < bus_interval:
        return bus_interval - elapsed
    else:
        return bus_interval - (elapsed % bus_interval)


if __name__ == '__main__':
    from sys import stdin

    start_time, late_time, n = _get_numbers()
    walk_times = _get_numbers()
    bus_times = _get_numbers()
    bus_intervals = _get_numbers()

    curr_time = start_time
    curr_time += walk_times[0]  # home to first bus stop
    for bus in range(n):
        curr_time += get_bus_wait(curr_time - start_time, bus_intervals[bus])
        curr_time += bus_times[bus]
        curr_time += walk_times[bus + 1]
    if curr_time <= late_time:
        print('yes')
    else:
        print('no')

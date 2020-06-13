# https://open.kattis.com/problems/bubbletea
# accepted answer, CPU time: 0.06s


"""
Sample input:
3
10 20 30
5
1 2 3 4 5
2 4 5
3 1 2 3
5 1 2 3 4 5
42

Sample output:
2

"""


def _get_numbers(first=False):
    """
    Gets a line of input from stdin and return the numbers in a list.
    If <first> is True, then return the first element of the list.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers[0] if first else numbers


if __name__ == '__main__':
    from sys import stdin

    num_teas = _get_numbers(True)

    tea_prices = _get_numbers()

    num_toppings = _get_numbers(True)

    topping_prices = _get_numbers()

    cheapest = float('inf')
    for tea in tea_prices:
        for topping in _get_numbers()[1:]:
            total = tea + topping_prices[topping - 1]
            if total < cheapest:
                cheapest = total

    money = _get_numbers(True)

    possible = max((money // cheapest) - 1, 0)
    print(possible)

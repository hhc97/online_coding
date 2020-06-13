# https://open.kattis.com/problems/bubbletea
# wrong answer


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


def find_cheapest_tea(tea_list: list) -> int:
    min_price = float('inf')
    for entry in tea_list:
        tea_price = entry[0]
        for topping in entry[1:]:
            if tea_price + topping < min_price:
                min_price = tea_price + topping
    return min_price


if __name__ == '__main__':
    from sys import stdin

    num_teas = _get_numbers(True)

    tea_prices = [[i] for i in _get_numbers()]

    num_toppings = _get_numbers(True)

    topping_prices = _get_numbers()

    for tea in tea_prices:
        tea.extend(_get_numbers()[1:])

    total_money = _get_numbers(True)

    cheapest_tea = find_cheapest_tea(tea_prices)
    print(cheapest_tea)

    print((total_money // cheapest_tea) - 1)

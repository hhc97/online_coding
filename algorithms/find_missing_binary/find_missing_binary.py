import itertools
import random


def generate_ages(bits: int) -> tuple:
    """
    Generates a (2 ** <bits>) long list of ages, removes one,
    shuffles it, and returns the list and the missing age.
    """
    lst = list(itertools.product([0, 1], repeat=bits))
    removed = random.choice(lst)
    lst.remove(removed)
    random.shuffle(lst)
    return lst, removed


def find_missing_age(ages: list) -> tuple:
    """
    Finds the missing age in <ages>.

    Precondition:
        <ages> is a list of n-bit binary tuples that represent the numbers
        [0, (2 ** n) - 1] with one tuple missing.

    >>> find_missing_age([(0, 1), (1, 1), (1, 0)])
    (0, 0)
    """
    missing = []

    curr_bit = 0
    while len(ages) > 1:
        zero_ptr, one_ptr = 0, 0
        for dino in ages:
            bit = dino[curr_bit]  # query the curr_bit
            if not bit:
                # if curr bit is 0, then swap it to the left side
                ages[zero_ptr], ages[one_ptr] = ages[one_ptr], ages[zero_ptr]
                zero_ptr += 1
            one_ptr += 1
        if zero_ptr % 2:  # odd number of 0's at curr_bit
            ages = ages[:zero_ptr]  # removes the ones
            missing.append(0)  # missing bit has a 0 at curr_bit
        else:  # odd number of 1's at curr_bit
            ages = ages[zero_ptr:]  # removes the zeros
            missing.append(1)  # missing bit has a 1 at curr_bit
        curr_bit += 1
    # add remaining bit to missing depending on last bit of last age
    missing.append(0 if ages[0][-1] else 1)
    return tuple(missing)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    age_list, missing_age = generate_ages(23)
    print('Missing age:', missing_age)
    found_age = find_missing_age(age_list)
    print('Found age:', found_age)
    assert found_age == missing_age, 'wrong age found'

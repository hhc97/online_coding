# https://open.kattis.com/problems/ladice


class UnionDrawer:
    """An augmented union find data structure to solve the problem"""

    def __init__(self, lst) -> None:
        """
        Takes in a list as an argument, and assumes each element is an individual set.
        Modifications for this application:
            Associate each set with a capacity.
        """
        self.parents = {i: None for i in lst}
        self.capacities = {i: 1 for i in lst}
        self.ranks = {i: 0 for i in lst}

    def get_parent(self, item):
        """
        Gets the parent of the set.
        It keeps a list of items that have been seen en route to the parent
        and sets their parent to the set's parent when done. (path compression)
        """
        path_list = []
        curr = item
        while self.parents[curr] is not None:
            path_list.append(curr)
            curr = self.parents[curr]
        for element in path_list:
            self.parents[element] = curr
        return curr

    def union(self, a, b) -> None:
        """Unions sets a and b."""
        a_parent = self.get_parent(a)
        b_parent = self.get_parent(b)
        if a_parent == b_parent:
            return
        a_rank = self.ranks[a_parent]
        b_rank = self.ranks[b_parent]
        if a_rank < b_rank:
            self.parents[a_parent] = b_parent
            self.capacities[b_parent] += self.capacities[a_parent]
        else:
            self.parents[b_parent] = a_parent
            self.capacities[a_parent] += self.capacities[b_parent]
            if a_rank == b_rank:
                self.ranks[a_parent] += 1

    def insert(self, set_elem) -> bool:
        """
        Inserts an element into the joint set, returns whether insertion
        was successful.
        """
        set_parent = self.get_parent(set_elem)
        if self.capacities[set_parent] > 0:
            self.capacities[set_parent] -= 1
            return True
        else:
            return False

    def debug(self):
        print(f'parents: {self.parents}')
        print(f'Capacities: {self.capacities}')
        print(f'Ranks: {self.ranks}\n')


def time_test():
    param = 300000
    test = UnionDrawer([i for i in range(1, param + 1)])
    import random
    for _ in range(param):
        first = random.randint(1, param)
        second = random.randint(1, param)
        test.union(first, second)
        test.get_parent(random.randint(1, param))


if __name__ == '__main__':
    from timeit import timeit

    time1 = timeit("time_test()", number=1, globals=globals())
    print(time1)

# if __name__ == '__main__':
#     first = input().split()
#     num_items, num_drawers = int(first[0]), int(first[1])
#     drawers = UnionDrawer([i for i in range(1, num_drawers + 1)])
#     for _ in range(num_items):
#         item_drawers = input().split()
#         drawer_a, drawer_b = int(item_drawers[0]), int(item_drawers[1])
#         drawers.union(drawer_a, drawer_b)
#         if drawers.insert(drawer_a):
#             print("LADICA")
#         else:
#             print("SMECE")

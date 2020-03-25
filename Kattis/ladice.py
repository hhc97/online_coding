# https://open.kattis.com/problems/ladice
# accepted answer, CPU time: 0.64s


class UnionDrawer:
    """An augmented union find data structure to solve the problem"""

    def __init__(self, n) -> None:
        """
        Takes in a list as an argument, and assumes each element is an individual set.
        Modifications for this application:
            Associate each set with a capacity.
        """
        self.parents = [i for i in range(n + 1)]
        self.capacities = [1] * (n + 1)
        self.ranks = [0] * (n + 1)

    def find(self, item):
        """
        Gets the parent of the set that contains <item>.
        It keeps a list of items that have been seen en route to the parent
        and sets their parent to the set's parent when done. (path compression)
        """
        if self.parents[item] == item:
            return item
        self.parents[item] = self.find(self.parents[item])
        return self.parents[item]

    def union(self, a, b) -> None:
        """Unions sets a and b."""
        a_parent = self.find(a)
        b_parent = self.find(b)
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
        set_parent = self.find(set_elem)
        if self.capacities[set_parent] > 0:
            self.capacities[set_parent] -= 1
            return True
        else:
            return False


if __name__ == '__main__':
    from sys import stdin, stdout

    first = stdin.readline().split()
    num_items, num_drawers = int(first[0]), int(first[1])
    drawers = UnionDrawer(num_drawers)
    output = []
    for _ in range(num_items):
        item_drawers = stdin.readline().split()
        drawer_a, drawer_b = int(item_drawers[0]), int(item_drawers[1])
        drawers.union(drawer_a, drawer_b)
        if drawers.insert(drawer_a):
            output.append("LADICA")
        else:
            output.append("SMECE")
    stdout.write("\n".join(output))

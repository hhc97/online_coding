# https://open.kattis.com/problems/millionairemadness


from heapq import heapify, heappush, heappop


def _get_numbers():
    """
    Gets a line of input from stdin and return the numbers in a list.
    If there is only 1 number, return the number itself.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers if len(numbers) > 1 else numbers[0]


def _make_adjacency_list(grid):
    d = {}
    max_row, max_col = len(grid), len(grid[0])

    def _get_vertex_num(row, col):
        return max_col * row + col + 1

    for i in range(max_row):
        for j in range(max_col):
            neighbors = {}
            for i2 in range(i - 1, i + 2):
                for j2 in range(j - 1, j + 2):
                    if i2 != i or j2 != j:
                        if 0 <= i2 < max_row and 0 <= j2 < max_col:
                            if i2 == i or j2 == j:
                                weight = abs(grid[i][j] - grid[i2][j2])
                                neighbors[_get_vertex_num(i2, j2)] = weight
            d[_get_vertex_num(i, j)] = neighbors
    return d


def prim(grid):
    """
    Uses Prim's algorithm to find a MST for <grid>.
    The MST is represented in the form of Dict[Int, Set[Int]].
    """
    adjacency_list = _make_adjacency_list(grid)
    mst = {}
    visited = {1}
    edges = [(w, 1, v) for v, w in adjacency_list[1].items()]
    heapify(edges)

    while edges:
        cost, frm, to = heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.setdefault(frm, set()).add(to)
            for to_next, cost in adjacency_list[to].items():
                if to_next not in visited:
                    heappush(edges, (cost, to, to_next))
    return mst


def invert_tree(mst):
    new_dict = {}
    for k, v in mst.items():
        for item in v:
            new_dict[item] = k
    return new_dict


def get_path(mst, start, end):
    tree = invert_tree(mst)
    path = [end]
    curr = end
    while curr != start:
        parent = tree[curr]
        path.append(parent)
        curr = parent
    return path[::-1]


if __name__ == '__main__':
    from sys import stdin, stdout

    output = []
    bank_vault = []

    num_rows, num_cols = _get_numbers()
    for _ in range(num_rows):
        bank_vault.append(_get_numbers())

    best_path = get_path(prim(bank_vault), 1, num_rows * num_cols)

    stdout.write("\n".join(output))

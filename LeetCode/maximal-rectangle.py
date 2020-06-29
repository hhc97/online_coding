# https://leetcode.com/problems/maximal-rectangle/

from typing import List


def maximal_rectangle(matrix: List[List[str]]) -> int:
    """
    >>> case1 = [["1","0","1","0","0"],
    ...          ["1","0","1","1","1"],
    ...          ["1","1","1","1","1"],
    ...          ["1","0","0","1","0"]]
    >>> maximal_rectangle(case1)
    6
    """

    def largest_rectangle_at_position(x: int, y: int) -> int:
        if matrix[x][y] == '0':
            return 0
        max_ones = 0
        while y + max_ones < num_cols and matrix[x][y + max_ones] == '1':
            max_ones += 1
        max_size = 0
        rows_seen = 0
        for row in matrix[x:]:
            row = row[y:y + max_ones]
            if '0' in row:
                zero_index = row.index('0')
                max_ones = zero_index
            if max_ones == 0:
                break
            rows_seen += 1
            curr_size = rows_seen * max_ones
            if curr_size > max_size:
                max_size = curr_size
        return max_size

    if not matrix:
        return 0
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    max_rectangle = 0
    for r in range(num_rows):
        for c in range(num_cols):
            rectangle_size = largest_rectangle_at_position(r, c)
            if rectangle_size > max_rectangle:
                max_rectangle = rectangle_size
    return max_rectangle


if __name__ == '__main__':
    import doctest

    doctest.testmod()

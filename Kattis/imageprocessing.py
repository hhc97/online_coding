# https://open.kattis.com/problems/imageprocessing
# accepted answer, CPU time: 0.06s


"""
Sample input:
4 4 2 2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
1 2
3 4

Sample output:
26 36 46
66 76 86
106 116 126

"""


def _get_numbers(first=False):
    """
    Gets a line of input from stdin and return the numbers in a list.
    If <first> is True, then return the first element of the list.
    """
    numbers = [int(v) for v in stdin.readline().split()]
    return numbers[0] if first else numbers


def _sum_position(img, ker, x, y):
    """Applies the kernel to img[x][y] and returns the result."""
    total = 0
    for i in range(len(ker)):
        for j in range(len(ker[0])):
            total += img[x + i][y + j] * ker[i][j]
    return total


def convolution(img, ker, height, width):
    """Applies the kernel to each pixel and returns the new image."""
    new_img = []
    ker = [row[::-1] for row in ker][::-1]
    for row in range(height):
        new_row = []
        for pixel in range(width):
            new_row.append(_sum_position(img, ker, row, pixel))
        new_img.append(new_row)
    return new_img


if __name__ == '__main__':
    from sys import stdin, stdout

    output = []

    h, w, n, m = _get_numbers()

    image, kernel = [], []

    for _ in range(h):
        image.append(_get_numbers())

    for _ in range(n):
        kernel.append(_get_numbers())

    transformed = convolution(image, kernel, h - n + 1, w - m + 1)

    for line in transformed:
        output.append(' '.join([str(num) for num in line]))

    stdout.write("\n".join(output))

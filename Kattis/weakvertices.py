# https://open.kattis.com/problems/weakvertices
# accepted answer, CPU time: 0.07s

if __name__ == '__main__':
    from sys import stdin, stdout

    running = True
    while running:
        n = int(stdin.readline())
        if n == -1:
            running = False
            break
        matrix = []
        weak_vertices = [True] * n
        for _ in range(n):
            matrix.append(stdin.readline().split())
        for row in range(n):
            neighbors = []
            for col in range(n):
                if matrix[row][col] == '1':
                    neighbors.append(col)
            for n1 in neighbors:
                for n2 in neighbors:
                    if matrix[n1][n2] == '1':
                        weak_vertices[row] = False
                        break
        weak_vertices2 = []
        for i in range(n):
            if weak_vertices[i]:
                weak_vertices2.append(str(i))
        stdout.write(' '.join(weak_vertices2) + '\n')

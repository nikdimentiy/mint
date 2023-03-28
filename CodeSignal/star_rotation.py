def solution(matrix, width, center, t):

    [r, c] = center
    offset = [(-1, -1), (-1, 0), (-1, 1), (0, 1),
              (1, 1), (1, 0), (1, -1), (0, -1)]
    print(offset)
    for d in range(1, width // 2 + 1):
        v = [matrix[r+d*i][c+d*j] for (i, j) in offset]
        v = v[-(t % 8):]+v[:-(t % 8)]
        for o, (i, j) in enumerate(offset):
            matrix[r+d*i][c+d*j] = v[o]

    return matrix

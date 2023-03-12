# CodeWars task - https://www.codewars.com/kata/63b84f54693cb10065687ae5/train/python

def create_box(m, n):
    matrix = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            dist_top = i
            dist_bottom = n - i - 1
            dist_left = j
            dist_right = m - j - 1
            matrix[i][j] = min(dist_top, dist_bottom,
                               dist_left, dist_right) + 1
    return matrix

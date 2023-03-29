def solution(matrix):
    field = {(x + y * 1j): v
             for y, row in enumerate(matrix)
             for x, v in enumerate(row)}
    return [[sum(field.get(p + i + j, 0) for i in (-1, 0, 1) for j in (-1j, 0, 1j)) - v
             for x, v in enumerate(row)
             for p in [x + 1j * y]]
            for y, row in enumerate(matrix)]

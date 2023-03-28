def solution(canvas, rectangle):
    x1, y1, x2, y2 = rectangle
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            if i == y1 or i == y2:
                canvas[i][j] = '*' if j == x1 or j == x2 else '-'
            elif j == x1 or j == x2:
                canvas[i][j] = '|'
    return canvas

def solution(image):
    rows = len(image)
    cols = len(image[0])
    blurred = [[0] * (cols - 2) for _ in range(rows - 2)]
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            avg = (image[i-1][j-1] + image[i-1][j] + image[i-1][j+1] +
                   image[i][j-1] + image[i][j] + image[i][j+1] +
                   image[i+1][j-1] + image[i+1][j] + image[i+1][j+1]) // 9
            blurred[i-1][j-1] = avg
    return blurred

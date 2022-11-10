def elevator_distance(array):
    dist = 0
    for i in range(len(array)-1):
        dist += abs(array[i] - array[i+1])
    return dist

def solution(a, b):
    if sorted(a) != sorted(b):
        return False
    else:
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
        return count <= 2

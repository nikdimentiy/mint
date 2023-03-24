def solution(ver1, ver2):
    ver1_fields = list(map(int, ver1.split('.')))
    ver2_fields = list(map(int, ver2.split('.')))

    for i in range(len(ver1_fields)):
        if ver1_fields[i] > ver2_fields[i]:
            return True
        elif ver1_fields[i] < ver2_fields[i]:
            return False

    # If we get here, both versions are equal
    return False

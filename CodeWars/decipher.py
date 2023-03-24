def solution(cipher):
    arr = list(map(int, cipher))
    curr = 0
    ret = []
    for num in arr:
        curr = curr * 10 + num
        if curr >= 97:
            ret.append(chr(curr))
            curr = 0
    return ''.join(ret)

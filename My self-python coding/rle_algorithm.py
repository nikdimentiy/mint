# def easy(s):
#     lastsym = s[0]
#     ans = []
#     for i in range(len(s)):
#         if s[i] != lastsym:
#             ans.append(lastsym)
#             lastsym = s[i]
#     ans.append(lastsym)
#     return "".join(ans)


def rle(s):
    def pack(s, cnt):
        if cnt > 1:
            return s + str(cnt)
        return s

    last_symbol = s[0]
    last_position = 0
    ans = []
    for i in range(len(s)):
        if s[i] != last_symbol:
            ans.append(pack(last_symbol, i - last_position))
            last_position = i
            last_symbol = s[i]
    ans.append(pack(s[last_position], len(s) - last_position))
    return "".join(ans)

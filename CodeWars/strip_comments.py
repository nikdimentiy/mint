def strip_comments(strng, markers):
    s = strng.split("\n")
    result = ""
    for i in s:
        trimmed = ""
        for j in i:
            if j not in markers:
                trimmed += j
            else:
                break
        trimmed = trimmed.rstrip()
        result = result + trimmed + "\n"
    return result[:-1]

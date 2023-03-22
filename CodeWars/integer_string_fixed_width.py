def solution(number, width):
    num_str = str(number)
    if len(num_str) >= width:
        return num_str[-width:]
    else:
        return "0"*(width-len(num_str)) + num_str

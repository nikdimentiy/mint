# CodeWars task - https://www.codewars.com/kata/63b84f54693cb10065687ae5/train/python


def create_box(m, n):  # m and n positive integers
    return [[min([x+1, y+1, m-x, n-y]) for x in range(m)] for y in range(n)]

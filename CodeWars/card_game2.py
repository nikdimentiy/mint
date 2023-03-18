# CodeWars task - https://www.codewars.com/kata/61fef3a2d8fa98021d38c4e5/python


def card_game(n):
    if n == 1:
        return 1
    t, s = 0, n+2
    while s > 3:
        s, t = s//2, t+1+s % 2
    return [n-t, t][n % 2]

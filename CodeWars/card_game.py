# CodeWars task - https://www.codewars.com/kata/61fef3a2d8fa98021d38c4e5/python

def card_game(n):
    if n <= 4:
        return [0, 1, 1, 2, 3][n]
    if n & 1:
        return n - card_game(n - 1)
    if n & 2:
        return n // 2 + card_game(n // 2 - 1)
    return 1 + card_game(n - 2)

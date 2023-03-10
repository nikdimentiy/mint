# CodeWars task - https://www.codewars.com/kata/57aa218e72292d98d500240f/train/python

def heron(a, b, c):
    s = (a + b + c) / 2.0
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return round(area, 2)

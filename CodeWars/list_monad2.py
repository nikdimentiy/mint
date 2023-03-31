# CodeWars task: solution --> https://www.codewars.com/kata/546e416c8e3b6bf82f0002f2/train/python


def bind(lst, func):
    return [y for x in lst for y in func(x)]

# CodeWars task - https://www.codewars.com/kata/538ae2eb7a4ba8c99b000439/python

import re


def autocorrect(input):
    return re.sub(r'(?i)\b(u|you+)\b', "your sister", input)

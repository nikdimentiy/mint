# CodeWars task: solution --> https://www.codewars.com/kata/52b2cf1386b31630870005d4/train/python

import re


def flesch_kincaid(text: str) -> float:
    """
    Calculate the Flesch-Kincaid grade level for a given string of text.

    The grade level is an approximation for what schoolchildren are able to understand a piece of text. 
    For example, a piece of text with a grade level of 7 can be read by seventh-graders and beyond.

    Args:
        text (str): The text to analyze.

    Returns:
        float: The Flesch-Kincaid grade level rounded to two decimal points.
    """
    def _words(s): return [''.join(c for c in w if c.isalpha)
                           for w in s.split()]

    def _syllables(ws): return sum(
        max(len(re.findall('[aeiou]+', w)), 1) for w in ws)
    sentences = [_words(s) for s in re.split(r'[.!?]+', text.lower()) if s]
    p1 = 0.39 / len(sentences) * sum(len(w) for w in sentences)
    p2 = 11.8 / sum(len(w) for w in sentences) * \
        sum(_syllables(s) for s in sentences)
    return round(p1 + p2 - 15.59, 2)

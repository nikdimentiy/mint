# CodeWars task - https://www.codewars.com/kata/54bb6f887e5a80180900046b/train/python


"""
***************************************
*   O(n) time complexity solution !   *
***************************************
"""


def longest_palindrome(s):

    maxPal, tmpPal = 0, 1
    count_dct = {}
    inPal = False

    for i, l in enumerate(s):

        count_dct[l] = count_dct.get(l, 0) + 1

        # might encounter a palindrome, there...
        if not inPal and count_dct[l] >= 2:
            # ... palindrome with double character in the middle
            if l == s[i-1]:
                inPal = True
                tmpPal = 2

            # ... palindrome with one "peak" character in the middle
            elif l == s[i-2]:
                inPal = True
                tmpPal = 3

        # still in a palindrome...
        elif inPal and l == s[max(0, i-tmpPal-1)]:
            tmpPal += 2

        else:                                          # goes out of this palindrome
            inPal = False
            tmpPal = 1

        maxPal = max(maxPal, tmpPal)

    return maxPal

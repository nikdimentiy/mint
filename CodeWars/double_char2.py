# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# double_char("String") ==> "SSttrriinngg"

# double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"

# double_char("1234!_ ") ==> "11223344!!__  "


def double_char(s):
    res = ''
    for i in s:
        res += i*2
    return res

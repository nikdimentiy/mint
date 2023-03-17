# CodeWars task - https://www.codewars.com/kata/6411b91a5e71b915d237332d/python


def valid_parentheses(x):
    while "()" in x:
        x = x.replace("()", "")
    return x == ""

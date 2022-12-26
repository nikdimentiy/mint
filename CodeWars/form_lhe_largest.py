# Given a number , Return The Maximum number could be formed from the digits of the number given.

# Notes

# Only Natural numbers passed to the function , numbers Contain digits [0:9] inclusive
# Digit Duplications could occur , So also consider it when forming the Largest


def max_number(n):
    return int("".join(sorted([i for i in str(n)], reverse=True)))

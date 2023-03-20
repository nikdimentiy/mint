# A step(x) operation works like this: it changes a number x into x - s(x),
# where s(x) is the sum of x's digits. You like applying functions to numbers, so given the number n,
# you decide to build a decreasing sequence of numbers: n, step(n), step(step(n)), etc., with 0 as the last element.

# Building a single sequence isn't enough for you, so you replace all elements of the sequence with the sums of their digits (s(x)).
# Now you're curious as to which number appears in the new sequence most often. If there are several answers, return the maximal one.

def step(x):
    return x - sum(int(digit) for digit in str(x))


def solution(n):
    sequence = [n]
    while sequence[-1] != 0:
        sequence.append(step(sequence[-1]))
    digit_sums = [sum(int(digit) for digit in str(x)) for x in sequence]
    freq = {}
    for digit_sum in digit_sums:
        freq[digit_sum] = freq.get(digit_sum, 0) + 1
    max_freq = max(freq.values())
    most_frequent = [
        digit_sum for digit_sum in freq if freq[digit_sum] == max_freq]
    return max(most_frequent)

# Let's call two integers A and B friends if each integer from the array divisors is either a divisor of both A and B or neither A nor B.
# If two integers are friends, they are said to be in the same clan. How many clans are the integers from 1 to k, inclusive, broken into?


def solution(divisors, k):
    clan = []
    for i in range(1, k+1):
        vec = []
        for j in range(0, len(divisors)):
            if i % divisors[j] == 0:
                vec.append(1)
            else:
                vec.append(0)
        clan.append(vec)

    clanSet = []
    for i in range(0, len(clan)):
        if clan[i] not in clanSet:
            clanSet.append(clan[i])

    return len(clanSet)

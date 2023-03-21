def solution(votes, k):
    m = max(votes)
    return sum(v + k > m for v in votes) if k > 0 else 1 if votes.count(m) == 1 else 0

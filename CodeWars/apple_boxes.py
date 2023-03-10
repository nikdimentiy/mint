# You have k apple boxes full of apples. Each square box of size m contains m × m apples.
# You just noticed two interesting properties about the boxes:

# The smallest box is size 1, the next one is size 2,..., all the way up to size k.
# Boxes that have an odd size contain only yellow apples. Boxes that have an even size contain only red apples.
# Your task is to calculate the difference between the number of red apples and the number of yellow apples.


def solution(k):
    yellow_apples = sum(i * i for i in range(1, k+1, 2))
    red_apples = sum(i * i for i in range(2, k+1, 2))
    return red_apples - yellow_apples

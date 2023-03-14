# Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size.
# Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1.
# He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.


def solution(statues):
    # sort the array in ascending order
    statues.sort()
    # initialize variables
    count = 0
    prev_statue = statues[0]
    # iterate through the array and count the differences
    for i in range(1, len(statues)):
        curr_statue = statues[i]
        diff = curr_statue - prev_statue
        if diff > 1:
            count += diff - 1
        prev_statue = curr_statue
    return count

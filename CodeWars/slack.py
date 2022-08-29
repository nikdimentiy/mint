from random import randint

my_random_scores = []

for num in range(10):
    my_random_scores.append(randint(0, 10))

print(my_random_scores)

my_min = my_random_scores[0]
count = 0

for num in my_random_scores:
    if my_min > num:
        my_min = num

for num in my_random_scores:
    if num == my_min:
        print(f"The first lowest score is {num} at position {count}")
        my_random_scores.pop(count)
        break
    count += 1

print(my_random_scores)

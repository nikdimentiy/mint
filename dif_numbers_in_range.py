# the code check a unique value in the range of numbers
numbers = [int(i) for i in input().split(' ')]
numbers.sort()
final = []
for i in range(len(numbers)):
    if len(numbers) == 1:
        final = [] 
    elif numbers[i] == numbers[i - 1]:
        if numbers[i] not in final:
            final.append(numbers[i])

for i in final:
    print(i, end=' ')

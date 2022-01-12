sequence_input = input()
answer = ""
answer_count = 0
for i in range(len(sequence_input)):
    now_count = 0
    for j in range(len(sequence_input)):
        if sequence_input[j] == sequence_input[i]:
            now_count += 1
    if now_count > answer_count:
        ans = sequence_input[i]
        answer_count = now_count
print(answer)

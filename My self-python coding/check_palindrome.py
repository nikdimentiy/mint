# the tiny code: analyzes whether the entered value is a palindrome
s = input()
# let's compare the elements of the sequence in pairs: the first with the last, the second with the penultimate...
i = 0
j = len(s) - 1 # calculate the length of the sequence and take the last element
is_polindrom = True
while i < j: # step by step compare the elements of the sequence by direction to the conditional middle
    if s[i] != s[j]:
        is_polindrom = False
    i += 1
    j -= 1
if is_polindrom:
    print("YES - entered value is palindrome!")
else:
    print("NO - this value in not palindrome!!!!")
   

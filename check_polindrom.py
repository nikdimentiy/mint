# the tiny code: analyzes whether the entered value is a palindrom
s = input()
i = 0
j = len(s) - 1
is_polindrom = True
while i < j:
    if s[i] != s[j]:
        is_polindrom = False
    i += 1
    j -= 1
if is_polindrom:
    print("YES - enterd value is polindrom!")
else:
    print("NO - this value in not polindrom!!!!")
   

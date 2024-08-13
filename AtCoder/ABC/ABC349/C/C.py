s = input()
t = input()
p = 0
for i in s:
    if i == t[p].lower():
        p += 1
    if p == 3:
        exit(print("Yes"))

if p == 2 and t[-1] == 'X':
    print("Yes")
else:
    print("No")
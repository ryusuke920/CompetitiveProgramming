s = list(map(int, list(input())))
#print(s)
a = b = 0
for i in range(14):
    if i % 2 == 0:
        a += s[i] * 3
    else:
        b += s[i]

if (a + b) % 10 == s[-1]:
    print("Yes")
else:
    print("No")
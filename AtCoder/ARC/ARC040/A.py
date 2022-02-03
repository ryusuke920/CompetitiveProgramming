n = int(input())
a = 0
b = 0
for i in range(n):
    s = str(input())
    for j in range(len(s)):
        if s[j] == "R":
            a += 1
        elif s[j] == "B":
            b += 1
if a == b:
    print("DRAW")
elif a > b:
    print("TAKAHASHI")
else:
    print("AOKI")
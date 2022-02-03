n = int(input())
r = str(input())
ans = 0
for i in r:
    if i == "A":
        ans += 4
    elif i == "B":
        ans += 3
    elif i == "C":
        ans += 2
    elif i == "D":
        ans += 1
print(ans/n)
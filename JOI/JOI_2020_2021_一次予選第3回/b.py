n = int(input())
s = input()
ans = 0
for i in range(n):
    if i%2 == 0:
        if s[i] != "I":
            ans += 1
    else:
        if s[i] != "O":
            ans += 1
print(ans)
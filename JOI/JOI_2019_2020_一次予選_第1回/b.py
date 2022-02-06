n = int(input())
s = input()
ch = "aiueo"
ans = 0
for i in range(n):
    if s[i] in ch:
        ans += 1
print(ans)
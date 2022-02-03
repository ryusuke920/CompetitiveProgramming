n = int(input())
s = list(input())
s = s[::-1]
ans = ""
for i in range(n):
    if s[i] not in ans:
        ans += s[i]
print(ans[::-1])
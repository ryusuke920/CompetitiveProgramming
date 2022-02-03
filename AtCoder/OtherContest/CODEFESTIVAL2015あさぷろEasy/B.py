n = int(input())
s = input()
if n%2 == 1:
    exit(print(-1))
ans = 0
for i in range(n//2):
    if s[i] != s[i+n//2]:
        ans += 1
print(ans)
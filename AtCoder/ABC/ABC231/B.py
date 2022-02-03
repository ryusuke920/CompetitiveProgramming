from collections import defaultdict

n = int(input())
s = [input() for _ in range(n)]

d = defaultdict(int)
for i in s:
    d[i] += 1

ans = ''
num = 0
for i in d:
    if num < d[i]:
        ans = i
        num = d[i]

print(ans)
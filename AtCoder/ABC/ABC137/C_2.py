from collections import defaultdict
n = int(input())
d = defaultdict(int)
cnt = 0
for i in range(n):
    s = sorted(input())
    s = str(s)
    cnt += d[s]
    d[s] += 1

print(cnt)
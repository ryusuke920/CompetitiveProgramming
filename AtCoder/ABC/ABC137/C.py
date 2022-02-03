from collections import defaultdict
n = int(input())
d = defaultdict(int)
count = 0
for i in range(n):
    s = "".join(sorted(input()))
    count += d[s]
    d[s] += 1
print(count)
from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for i in a:
    d[i] += 1

for i in d:
    if d[i] != 4:
        print(i)
        break
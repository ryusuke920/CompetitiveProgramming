from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for i in a:
    d[i] += 1

ans = 0
for i in range(1, 10 ** 5 // 2 + 1):
    ans += d[i] * d[10 ** 5 - i] if i != 50000 else d[50000] * (d[50000] - 1) // 2

print(ans)
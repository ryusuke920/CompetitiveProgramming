from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

ans = [0] * (2 ** n)
rev = defaultdict(int)
for i in range(2 ** n):
    rev[a[i]] = i

ans[rev[2 ** n]] = n

for i in range(n):
    winner = []
    for j in range(2 ** (n - i - 1)):
        p, q = a[2 * j], a[2 * j + 1]
        winner.append(max(p, q))
        ans[rev[min(p, q)]] = i + 1
    a = winner


print(*ans, sep='\n')
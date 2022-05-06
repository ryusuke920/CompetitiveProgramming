def divisors(n):
    divisor = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor.append(i)
            if i != n // i:
                divisor.append(n // i)

    divisor.sort()
    return divisor

from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for i in a:
    d[i] += 1

ans = 0
for i in range(n):
    div = divisors(a[i])
    l = len(div)
    for a_j in div:
        a_k = a[i] // a_j
        ans += d[a_j] * d[a_k]

print(ans)
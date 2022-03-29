from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))

sum_ = [0] * (n + 1)
for i in range(n):
    sum_[i + 1] = sum_[i] + a[i]

d = defaultdict(int)
d[0] = 1
ans = 0
for i in range(n):
    ans += d[sum_[i + 1] % m]
    d[sum_[i + 1] % m] += 1

print(ans)
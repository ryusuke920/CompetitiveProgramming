from bisect import bisect_right

n, q = map(int, input().split())
a = sorted(list(map(int, input().split())))

s = [0] * (n + 1)
for i in range(n):
    s[i + 1] = a[i] + s[i]

sum_ = sum(a)

for _ in range(q):
    x = int(input())
    t = bisect_right(a, x)
    print(sum_ - 2 * s[t] + (2 * t - n) * x)
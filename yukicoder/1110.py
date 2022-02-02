from bisect import bisect_right

n, d = map(int, input().split())
a = [int(input()) for _ in range(n)]
p = [i for i in a]
p.sort()

# Ai - d >= aj
for i in range(n):
    t = bisect_right(p, a[i] - d)
    print(t)
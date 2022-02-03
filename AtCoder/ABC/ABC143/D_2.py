from bisect import bisect_left
n = int(input())
l = list(map(int,input().split()))
l.sort()
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        num = l[i] + l[j]
        t = bisect_left(l, num)
        if t > j:
            ans += t - j - 1

print(ans)
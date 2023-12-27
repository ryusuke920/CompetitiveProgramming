from bisect import bisect_left, bisect_right

n, m, d = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
b.append(10**20)
#print(b)
ans = -1
for i in range(n):
    t = bisect_right(b, a[i] + d)
    if abs(a[i] - b[t - 1]) <= d:
        ans = max(ans, a[i] + b[t - 1])
   # print(i,ans,t)

print(ans)
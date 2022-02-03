from collections import defaultdict
n, k = map(int,input().split())
a = list(map(int,input().split()))

d = defaultdict(int)
for i in range(k):
    d[a[i]] += 1

ans = len(d)

cnt = ans
for i in range(n - k):    
    if d[a[i]] == 1:
        cnt -= 1
    d[a[i]] -= 1
    if d[a[i + k]] == 0:
        cnt += 1
    d[a[i + k]] += 1
    ans = max(ans, cnt)

print(ans)
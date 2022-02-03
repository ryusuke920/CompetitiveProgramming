n,k,m,r = map(int,input().split())
s = [int(input()) for _ in range(n-1)]
s.sort(reverse = True)
before = sum(s[:k])
mid = sum(s[:k - 1])
import math
if before >= k*r:
    exit(print(0))
elif mid + m < k*r:
    exit(print(-1))
else:
    ans = math.ceil(k*r - mid)
    print(ans)
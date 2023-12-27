from heapq import heapify, heappop, heappush

n = int(input())
a = list(map(int, input().split()))

pq1 = [a[i] for i in range(n)]
heapify(pq1)
ans1 = [0] * (n + 1)
sum_ = sum(pq1)
ans1[0] = sum_
for i in range(n):
    v = heappop(pq1)
    if a[i + n] > v:
        heappush(pq1, a[i + n])
        sum_ -= v
        sum_ += a[i + n]
    else:
        heappush(pq1, v)
    ans1[i + 1] = sum_
    
ans2 = [0] * (n + 1)
pq2 = [-a[-1 - i] for i in range(n)]
heapify(pq2)
sum_ = sum(pq2)
ans2[n] = -sum_
for i in range(n):
    v = -heappop(pq2)
    if a[-1 - i - n] < v:
        heappush(pq2, -a[-1 - i - n])
        sum_ += v
        sum_ -= a[-1 - i - n]
    else:
        heappush(pq2, -v)
    ans2[n - i - 1] = -sum_

ans = -10**18
for i in range(n + 1):
    ans = max(ans, ans1[i] - ans2[i])

print(ans)
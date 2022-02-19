from itertools import product

n, t = map(int, input().split())
a = list(map(int, input().split()))

cnt = min(n, 20)
time1 = [0] # 時間を入れる配列
for i in product([0, 1], repeat=cnt):
    num = 0
    for j in range(cnt):
        if i[j] == 1:
            num += a[j]
    
    if num <= t:
        time1.append(num)

time1 = sorted(list(set(time1)))

cnt = max(0, n - 20)
time2 = [0]
for i in product([0, 1], repeat=cnt):
    num = 0
    for j in range(cnt):
        if i[j] == 1:
            num += a[j + 20]
    
    if num <= t:
        time2.append(num)

time2 = sorted(list(set(time2)))
time1.append(10 ** 20)
time2.append(10 ** 20)
#print(time1)
#print(time2)
from bisect import bisect_right
ans = 0
for i in time1:
    p = bisect_right(time2, t - i)
    cnt = i + time2[p - 1]
    if cnt <= t:
        ans = max(ans, cnt)

print(ans)
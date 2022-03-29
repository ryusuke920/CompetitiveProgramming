from collections import defaultdict, deque

n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
now = 0 # 今見る場所
d = defaultdict(int)
roop = deque([])
num = []
i = 0
while True:
    ans += a[now]
    roop.append(a[now])
    d[now] += 1
    if d[now] == 2:
        break
    now = ans % n
    if i == k - 1:
        exit(print(ans))
    i += 1

#print(roop)
#print(now)
before_roop = []
for _ in range(len(roop)):
    if roop[0] != roop[-1]:
        before_roop.append(roop[0])
        roop.popleft()
    else:
        break

roop.pop()
#print(before_roop)
#print(roop)
roop_sum = 0
for i in roop:
    roop_sum += i
l = len(roop)
#print(roop, before_roop)
l_before = len(before_roop)
if k <= l_before:
    ans = 0
    for i in range(k):
        ans += before_roop[i]
    print(ans)
else:
    ans = sum(before_roop)
    k -= l_before
    p = k // l
    q = k % l
    ans += roop_sum * p
    for i in range(q):
        ans += roop[i]
    print(ans)
from bisect import bisect_right

n = int(input())
a = [int(input()) for _ in range(n)]

ma = max(a)
score = [0] * (ma + 1)
for i in range(n):
    if a[i] == 0: continue
    score[-1 - a[i]] += 1

for i in range(ma):
    score[i + 1] += score[i]

for _ in range(int(input())):
    q = int(input())
    t = bisect_right(score, q)
    print(ma - t + 1)
n = int(input())
r = list(map(int,input().split()))

p = [r[0]]
for i in range(1, n):
    if r[i] != p[-1]:
        p.append(r[i])

ans = [p[0]]
for i in range(1, len(p) - 1):
    if p[i - 1] < p[i] > p[i + 1] or p[i - 1] > p[i] < p[i + 1]:
        ans.append(p[i])

if len(ans) < 2:
    print(0)
else:
    print(len(ans) + 1)
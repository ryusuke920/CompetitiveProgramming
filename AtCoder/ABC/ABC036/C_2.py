n = int(input())
a = [int(input()) for _ in range(n)]
d = {}
for i in range(n):
    if a[i] not in d:
        d[a[i]] = 1
    else:
        d[a[i]] += 1
ans = [0] * n
for i, j in enumerate(sorted(d.keys())):
    for k in d[j]:
        ans[k] = i
print(ans)
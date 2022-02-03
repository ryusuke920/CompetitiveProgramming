n = int(input())
d = {}
for i in range(n):
    a = int(input())
    if a in d:
        d[a].append(i)
    else:
        d[a] = [i]
ans = [0] * n
print(d)
for i, j in enumerate(sorted(d.keys())):
    for k in d[j]:
        ans[k] = i
print(ans)
for i in range(len(ans)):
    print(ans[i])
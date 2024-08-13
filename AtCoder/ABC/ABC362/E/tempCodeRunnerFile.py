s = set()
for i in range(N):
    for j in range(i, N):
        s.add((A[i], A[j] - A[i]))

d = {}
for i in A:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

ans = [0]*1000
for i, j in s:
    if j == 0:
        for k in range(1, d[i] + 1):
            ans[i] += combination(d[i], k)
        continue
    f(i, j)

ans[1] = N
print(*ans[1:N + 1])
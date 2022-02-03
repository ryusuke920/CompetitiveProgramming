n, m = map(int,input().split())
a = [[0] * m for _ in range(n)]
for i in range(n):
    k = list(map(int,input().split()))
    for j in range(1, len(k)):
        a[i][k[j] - 1] = 1

p, q = map(int,input().split())
b = list(map(int,input().split()))

ans = 0
for i in range(n):
    cnt = 0
    for j in range(m):
        if j + 1 in b and a[i][j] == 1:
            cnt += 1
    if cnt >= q:
        ans += 1

print(ans)
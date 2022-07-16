t, n = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(t)]

ans = sum(p[0])
print(ans)
cnt = ans
for i in range(1, t):
    for j in range(n):
        if p[i][j] > p[0][j]:
            cnt += p[i][j] - p[0][j]
            p[0][j] = p[i][j]
    print(cnt)
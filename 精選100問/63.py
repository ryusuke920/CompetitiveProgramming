n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            if a[i][k] > a[i][j] + a[j][k]:
                exit(print(-1))

ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        Bool = True
        for k in range(n):
            if i == k or j == k: continue
            if a[i][j] == a[i][k] + a[k][j]:
                Bool = False
                break
        
        if Bool:
            ans += a[i][j]

print(ans)
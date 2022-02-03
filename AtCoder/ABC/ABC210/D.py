h, w, c = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]
ans = 10 ** 18
for i in range(h):
    cnt = a[i][0]
    for j in range(w - 1):
        ans = min(ans, a[i][j + 1] + cnt + c)
        cnt = min(a[i][j + 1], cnt + c)
    
    if i != h - 1:
        for j in range(w):
            ans = min(ans, a[i + 1][j] + a[i][j] + c)
            a[i + 1][j] = min(a[i + 1][j], a[i][j] + c)

print(ans)
h, w = map(int,input().split())
mi = 1000
a = [list(map(int,input().split())) for _ in range(h)]
for i in range(h):
    for j in range(w):
        mi = min(mi, a[i][j])
ans = 0
for i in range(h):
    for j in range(w):
        ans += max(0, a[i][j] - mi)
print(ans)
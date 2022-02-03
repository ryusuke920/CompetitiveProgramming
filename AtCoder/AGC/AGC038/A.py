h, w, a, b = map(int,input().split())
ans = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if 0 <= i <= b - 1:
            if 0 <= j <= a - 1:
                ans[i][j] = 0
            else:
                ans[i][j] = 1
        else:
            if 0 <= j <= a - 1:
                ans[i][j] = 1
            else:
                ans[i][j] = 0

for i in range(h):
    print(*ans[i], sep = "")
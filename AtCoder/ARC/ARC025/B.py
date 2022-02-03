h, w = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]

# 黒だけの配列を作る
black = [[0] * (w + 1) for _ in range(h + 1)]
for i in range(h):
    for j in range(w):
        if (i + j) % 2 != 0: continue
        black[i + 1][j + 1] = a[i][j]

# 黒のみの２次元累積和を取る
for i in range(h):
    for j in range(w - 1):
        black[i + 1][j + 2] += black[i + 1][j + 1]

for i in range(w):
    for j in range(h - 1):
        black[j + 2][i + 1] += black[j + 1][i + 1]


# 白だけの配列を作る
white = [[0] * (w + 1) for _ in range(h + 1)]
for i in range(h):
    for j in range(w):
        if (i + j) % 2 != 1: continue
        white[i + 1][j + 1] = a[i][j]

# 白のみの２次元累積和を取る
for i in range(h):
    for j in range(w - 1):
        white[i + 1][j + 2] += white[i + 1][j + 1]

for i in range(w):
    for j in range(h - 1):
        white[j + 2][i + 1] += white[j + 1][i + 1]

s = [[0] * (w + 1) for _ in range(h + 1)]
for i in range(h + 1):
    for j in range(w + 1):
        s[i][j] = black[i][j] - white[i][j]

ans = 0
for i in range(h): # 縦の手前
    for j in range(w): # 横の手前
        for ii in range(i, h + 1): # 縦の奥
            for jj in range(j, w + 1): # 横の奥
                if s[ii][jj] - s[i][jj] - s[ii][j] + s[i][j] == 0:
                    ans = max(ans, (ii - i) * (jj - j))

print(ans)
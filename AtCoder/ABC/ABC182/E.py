from sys import stdin
h,w,n,m = map(int,input().split())
grid1 = [[0] * w for _ in range(h)] # 横用
grid2 = [[0] * w for _ in range(h)] # 縦用
ab = [list(map(lambda x: int(x) - 1, stdin.readline().split())) for _ in range(n)]
cd = [list(map(lambda x: int(x) - 1, stdin.readline().split())) for _ in range(m)]

for i in range(m):
    grid1[cd[i][0]][cd[i][1]] = -1 # ブロックの場所を-1にする
    grid2[cd[i][0]][cd[i][1]] = -1 # ブロックの場所を-1にする

# 横の処理
for i in range(n):
    # 左に進む
    x1 = x2 = 0 # 左・右
    if grid1[ab[i][0]][ab[i][1]] != 1:
        while ab[i][1] - x1 > 0:
            grid1[ab[i][0]][ab[i][1]] = 1
            x1 += 1
            if grid1[ab[i][0]][ab[i][1] - x1] == -1: break
            else:
                grid1[ab[i][0]][ab[i][1] - x1] = 1
        # 右に進む
        while ab[i][1] + x2 < w - 1:
            grid1[ab[i][0]][ab[i][1]] = 1
            x2 += 1
            if grid1[ab[i][0]][ab[i][1] + x2] == -1: break
            else:
                grid1[ab[i][0]][ab[i][1] + x2] = 1
    else: continue

# 縦の処理
for i in range(n):
    # 上に進む
    y1 = y2 = 0 # 上・下
    if grid2[ab[i][0]][ab[i][1]] != 1:
        while ab[i][0] - y1 > 0:
            grid2[ab[i][0]][ab[i][1]] = 1
            y1 += 1
            if grid2[ab[i][0] - y1][ab[i][1]] == -1: break
            else:
                grid2[ab[i][0] - y1][ab[i][1]] = 1
        # 下に進む
        while ab[i][0] + y2 < h - 1:
            grid2[ab[i][0]][ab[i][1]] = 1
            y2 += 1
            if grid2[ab[i][0] + y2][ab[i][1]] == -1: break
            else:
                grid2[ab[i][0] + y2][ab[i][1]] = 1
    else: continue

ans = 0
for i in range(h):
    for j in range(w):
        if grid1[i][j] + grid2[i][j] >= 1:
            ans += 1
print(ans)
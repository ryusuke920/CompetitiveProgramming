h, w = map(int,input().split())
s = [list(input()) for _ in range(h)]

check = [["."] * w for _ in range(h)] # 仮に塗る
d = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]] # ８方向に対する変化量
for i in range(h):
    for j in range(w):
        cnt = 0 # 条件を満たせば + 1
        num = 0 # みた個数
        for dy, dx in d:
            
            if not (0 <= dy + i <= h - 1 and 0 <= dx + j <= w - 1): continue
            
            num += 1
            if s[dy + i][dx + j] == "#":
                cnt += 1
        
        num += 1
        if s[i][j] == "#":
            cnt += 1

        if cnt == num:
            check[i][j] = "#"

ans = [["."] * w for _ in range(h)] # 実際にcheckを塗ってsと重なるかを確かめる
for i in range(h):
    for j in range(w):
        if check[i][j] == "#":
            ans[i][j] = "#"
            for dy, dx in d:
                if not (0 <= dy + i <= h - 1 and 0 <= dx + j <= w - 1): continue
                ans[dy + i][dx + j] = "#"

if ans == s:
    print("possible")
    for i in range(h):
        print(*check[i], sep = "")
else:
    print("impossible")
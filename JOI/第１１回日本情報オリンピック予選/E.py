from collections import deque
w, h = map(int,input().split())
grid = [['0'] * (w + 2) for _ in range(h + 2)]

for i in range(h):
    S = list(input())
    for j in range(w):
        grid[i + 1][j + 1] = S[2 * j] # 文字列で取ってるので ' ' も含まれるから 2 * j とする

check = [[-1] * (w + 2) for _ in range(h + 2)]
d = [[1, 0], [-1, 0], [0, 1], [0, -1]] # 行けるかどうかチェックする際に使用する４方向の変化量
q = deque()
q.append([0, 0])
check[0][0] = 0

odd_d = [[-1, 0], [0, -1], [1, 0], [1, 1], [0, 1], [-1, 1]] # 奇数行６近傍の変化量 (y, x)
even_d = [[-1, -1], [0, -1], [1, -1], [1, 0], [0, 1], [-1, 0]] # 偶数行６近傍の変化量 (y, x)

# BFSで行ける場所を調べ上げる（-1 = 行けない, 0 = 行ける）
while q:
    v = q.popleft()
    if v[0] % 2 == 0:
        for i, j in even_d: # (dy, dx)
            if not (0 <= v[0] + i <= h + 1 and 0 <= v[1] + j <= w + 1): continue # 範囲外は調べない
            if grid[v[0] + i][v[1] + j] == '1': continue # 行く先が建物である場合には調べない
            if check[v[0] + i][v[1] + j] != -1: continue # 既にチェック済みの場所は調べない
            q.append([v[0] + i, v[1] + j])
            check[v[0] + i][v[1] + j] = 0
    else: # v[1] % 2 == 0:
        for i, j in odd_d: # (dy, dx)
            if not (0 <= v[0] + i <= h + 1 and 0 <= v[1] + j <= w + 1): continue # 範囲外は調べない
            if grid[v[0] + i][v[1] + j] == '1': continue # 行く先が建物である場合には調べない
            if check[v[0] + i][v[1] + j] != -1: continue # 既にチェック済みの場所は調べない
            q.append([v[0] + i, v[1] + j])
            check[v[0] + i][v[1] + j] = 0

# 周囲全てが黒で覆われているものは１に書き換える（入力例１だと (3, 2) など）
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if check[i][j] == -1: # checkが -1 であれば全ての周囲が建物であるので'1'に置き換える
            grid[i][j] = '1'

ans = 0

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if grid[i][j] == '1': # 今いるマスが建物であれば計算を開始する
            cnt = 0
            if i % 2 == 0: # 偶数行のとき（even_dを使うとき）
                for k in range(6):
                    if grid[i + even_d[k][0]][j + even_d[k][1]] == '1':
                        cnt += 1
            else: # 奇数行のとき（odd_dを使うとき）
                for k in range(6):
                    if grid[i + odd_d[k][0]][j + odd_d[k][1]] == '1':
                        cnt += 1
            ans += 6 - cnt # ６箇所のうち建物である場所を引けば装飾するべき場所が求まる

print(ans)
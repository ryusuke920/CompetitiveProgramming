from collections import deque
h, w, n = map(int,input().split()) # gridマスの縦、横、チーズの数
grid = [[] for _ in range(h)]
for i in range(h):
    S = list(input())
    grid[i] = S

num = [str(i + 1) for i in range(n)] # チーズを探す際に作っておくと楽になる
q = deque() # (y, x)
cheese = [[0, 0] for _ in range(n)] # それぞれのチーズのある場所を記録する配列（y座標・x座標）
for i in range(h):
    for j in range(w):
        for k in range(n):
            if grid[i][j] == num[k]:
                (cheese[k][0], cheese[k][1]) = (i, j) # それぞれの番号（チーズ）がある場所を記録する
        if grid[i][j] == "S": # スタート地点をdequeに追加する
            q.append([i, j])

d = [[1, 0], [-1, 0], [0, 1], [0, -1]] # ４方向への変化量
ans = 0 # 距離を足していくもの（いわゆる答え）
for k in range(n): # n回分チーズを食べる
    if k != 0: # i == 0 のときは既に16, 17行目でdequeに追加している
        q = deque() # (y, x)
        q.append([cheese[k - 1][0], cheese[k - 1][1]]) # n回ごとのスタート地点を決める
    dist = [[10000] * w for _ in range(h)] # boolの役割もしている
    dist[q[0][0]][q[0][1]] = 0 # スタート地点は0距離
    while q:
        v = q.popleft()
        for i, j in d:
            if not (0 <= v[0] + i <= h - 1 and 0 <= v[1] + j <= w - 1): continue # 行く先が範囲外なら調べない
            if grid[v[0] + i][v[1] + j] == "X": continue # 障害物の場合は調べない
            if dist[v[0] + i][v[1] + j] != 10000: continue # 既に調べている場所は調べない
            q.append([v[0] + i, v[1] + j]) # 次の場所をdequeに追加する
            dist[v[0] + i][v[1] + j] = dist[v[0]][v[1]] + 1 # １歩先の場所は今いる場所から +1 して更新する
            if grid[v[0] + i][v[1] + j] == str(k + 1): # ゴール地点が見つかったらwhile文を脱出
                ans += dist[v[0] + i][v[1] + j] # スタートからゴールまでかかった分を足す
                break
print(ans)
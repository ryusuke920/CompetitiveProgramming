from collections import deque
while True:
    w, h = map(int,input().split())
    if (w, h) == (0, 0):
        exit()
    x = [[0] * w for _ in range(h - 1)] # 横線の障害物（0 = 何もない, 1 = 壁あり）
    y = [[0] * (w - 1) for _ in range(h)] # 縦線の障害物（0 = 何もない, 1 = 壁あり）

    for i in range(2 * h - 1): # 入力を受け取る
        S = list(map(int,input().split()))
        if i % 2 == 0: # 縦線の有無
            for j in range(w - 1):
                y[i // 2][j] = S[j]
        else: # 横線の有無
            for j in range(w):
                x[i // 2][j] = S[j]

    dist = [[10000] * w for _ in range(h)] # 初期値は10000で設定（boolの役割も果たせる）
    dist[0][0] = 1 # スター地点は距離１でいける
    q = deque()
    q.append([0, 0]) # スタート地点は左上の[0, 0]（y・x）
    d = [[1, 0], [-1, 0], [0, 1], [0, -1]] # ４方向に対する変化量
    while q:
        v = q.popleft()
        for dy, dx in d:
            if not (0 <= v[0] + dy <= h - 1 and 0 <= v[1] + dx <= w - 1): continue # 範囲外であれば調べない
            if dist[v[0] + dy][v[1] + dx] != 10000: continue # 既にチェック済みの場所は調べない
            if dx == 0: #今調べてるのが縦（y）方向に行けるかどうかの場合
                if dy >= 0:
                    if x[v[0]][v[1]] == 1: continue # 壁のときは行けないので調べない
                else:
                    if x[v[0] + dy][v[1]] == 1: continue # 壁のときは行けないので調べない
                dist[v[0] + dy][v[1] + dx] = dist[v[0]][v[1]] + 1 # 今いる場所 +1 する
                q.append([v[0] + dy, v[1] + dx]) # 新たに行けた場所をdequeに追加する               
            else: #今調べてるのが横（x）方向に行けるかどうかの場合
                if dx >= 0:
                    if y[v[0]][v[1]] == 1: continue # 壁のときは行けないので調べない
                else:
                    if y[v[0]][v[1] + dx] == 1: continue # 壁のときは行けないので調べない
                dist[v[0] + dy][v[1] + dx] = dist[v[0]][v[1]] + 1 # 今いる場所 +1 する
                q.append([v[0] + dy, v[1] + dx]) # 新たに行けた場所をdequeに追加する

    if dist[-1][-1] == 10000: # 更新されてない場合は行けないことを意味している
        print(0)
    else:
        print(dist[-1][-1])
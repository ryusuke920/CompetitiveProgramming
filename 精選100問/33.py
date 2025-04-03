from collections import deque
h, w = map(int,input().split())
s = [[] for _ in range(h)]
for i in range(h):
    S = list(input())
    for j in range(w):
        s[i].append(S[j])

# マス全体の白いマスの個数を計算する
white = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            white += 1

dist = [[10000] * w for _ in range(h)] # 各マスの距離を記録する配列
q = deque()
q.append([0, 0]) # スタート地点は(0(x座標), 0(y座標))
dist[0][0] = 1 # スタート地点は白いので +1 しておく
d = [[1, 0], [-1, 0], [0, 1], [0, -1]] # ４方向に対する変化量
while q:
    v = q.popleft()
    for i, j in d:
        if not (0 <= v[0] + i <= h - 1 and 0 <= v[1] + j <= w - 1): continue # 行く先が範囲外なら調べない
        if s[v[0] + i][v[1] + j] == "#": continue # 黒の場合は調べない
        if dist[v[0] + i][v[1] + j] != 10000: continue # 既に調べている場所は調べない
        q.append([v[0] + i, v[1] + j]) # 新しく行く場所をdequeに追加する
        dist[v[0] + i][v[1] + j] = dist[v[0]][v[1]] + 1

last = dist[-1][-1]
if dist[-1][-1] == 10000: # 距離が更新されていないのでたどり着けない
    print(-1)
else:
    print(white - last) # 解 = （全体の白色の個数） - （通らなければならない白い場所）
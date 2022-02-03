from collections import deque
import sys
input = sys.stdin.readline
grid = [list(input()) for _ in range(10)]

sea = [] # 100マスのうちの海の場所を格納する配列
# 海の場所を調べる
for i in range(10):
    for j in range(10):
        if grid[i][j] == "x":
            sea.append([i, j]) # y, x


# 海を陸にした場合のbfs, スタートは陸にした場所から
def bfs(sy, sx):
    check = [[False] * 10 for _ in range(10)] # False -> 海, True -> 陸
    check[sy][sx] = True # 0index
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]] # ４方向への変化量
    q = deque() # dequeの生成
    q.append([sy, sx]) # スタート地点をキューに追加
    while q: # qがカラになるまで
        v = q.popleft() # 今いる場所のy, x
        for dy, dx in d:
            if not (0 <= v[0] + dy <= 9 and 0 <= v[1] + dx <= 9): continue # 配列外参照を避ける
            if not (grid[v[0] + dy][v[1] + dx] == "o"): continue # 行く先が土でなければ調べない
            if check[v[0] + dy][v[1] + dx] != False: continue # Trueであれば調べない（既に調べてあるから）
            check[v[0] + dy][v[1] + dx] = True # 調べ済みにする
            q.append([v[0] + dy, v[1] + dx]) # キューに新たに追加する
    
    # 全てのマスを調べ終わったら、陸かつFalse (= 繋がっていない)場所がないかを調べる
    ans = True
    for i in range(10):
        for j in range(10):
            if check[i][j] == False and grid[i][j] == "o" and ans == True:
                ans = False # NO
    return ans # boolでreturn

for i in range(len(sea)):
    Bool = bfs(sea[i][0], sea[i][1])
    if Bool:
        exit(print("YES"))
else:
    print("NO")
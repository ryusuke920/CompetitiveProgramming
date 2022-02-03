from collections import deque
import sys
from typing import Tuple
input = sys.stdin.readline
a = [list(input()) for _ in range(10)]
sea = []
for i in range(10):
    for j in range(10):
        if a[i][j] == 'x':
            sea.append([i, j]) # 海のy, x 座標

def bfs(sy, sx):
    check = [[False] * 10 for _ in range(10)]
    q = deque()
    q.append([sy, sx]) # スタート地点をキューに追加
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 上下左右の変化量(y, x)
    check[sy][sx] = True
    while q:
        v = q.popleft() # 現在地
        for dy, dx in d:
            if not (0 <= v[0] + dy <= 9 and 0 <= v[1] + dx <= 9): continue # 配列外参照
            if a[v[0] + dy][v[1] + dx] != 'o': continue # 海の時行けない
            if check[v[0] + dy][v[1] + dx] == False:
                check[v[0] + dy][v[1] + dx] = True # 陸に行くことができる
                q.append([v[0] + dy, v[1] + dx]) # 新しくキューに追加
    ans = True
    for i in range(10):
        for j in range(10):
           if check[i][j] == False and a[i][j] == 'o':
                ans = False
    return ans

for i in range(len(sea)):
    Bool = bfs(sea[i][0], sea[i][1])
    if Bool:
        exit(print('YES'))
print('NO')
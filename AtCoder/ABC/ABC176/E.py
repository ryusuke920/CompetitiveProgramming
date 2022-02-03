from collections import defaultdict
import sys
input = sys.stdin.readline
h, w, m = map(int,input().split())
bom = defaultdict(int)
y = [0] * h
x = [0] * w
for i in range(m):
    Y, X = map(int,input().split())
    y[Y - 1] += 1 # 爆弾のあるy座標をカウントする
    x[X - 1] += 1 # 爆弾のあるx座標をカウントする
    bom[(Y - 1) * 10 ** 9 + (X - 1)] += 1

ma_h = max(y)
ma_w = max(x)
ans = ma_h + ma_w

# yの最大値のある場所
s = []
for i, j in enumerate(y):
    if j == ma_h:
        s.append(i)

# xの最大値のある場所
t = []
for i, j in enumerate(x):
    if j == ma_w:
        t.append(i)

# 爆弾の中に最大値の場所があるかを考える
for i in s:
    for j in t:
        if bom[i * 10 ** 9 + j] == 0: # 1でない場所がある = そこにおけば最大値にできる
            exit(print(ans))
print(ans - 1)
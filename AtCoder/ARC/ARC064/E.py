from math import sqrt
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
xs, ys, xt, yt = map(int,input().split())
n = int(input())
x = [0] * (n + 2) # n個の円と始点と終点
y = [0] * (n + 2) # n個の円と始点と終点
r = [0] * (n + 2) # n個の円と始点と終点
(x[0], y[0], r[0]) = (xs, ys, 0)
(x[-1], y[-1], r[-1]) = (xt, yt, 0)

for i in range(n):
    x[i + 1], y[i + 1], r[i + 1] = map(int,input().split())

graph = [[] for _ in range(n + 2)] # n個の円と始点と終点
for i in range(n + 2):
    for j in range(n + 2):
        if i == j:
            num = 0
        else:
            num = max(0, sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) - (r[i] + r[j]))
        graph[i].append((j,num)) # ノード・距離

dist = [10 ** 18] * (n + 2)
q = [(0, 0)] # 距離・ノード（スタートは0）
dist[0] = 0 # 始点の距離は0
while q:
    v = heappop(q) # 今いる所までの距離・今いるノード
    if dist[v[1]] < v[0]: continue # これが枝刈りか〜〜
    for i, j in graph[v[1]]: # 先のノード・先までの距離
        if dist[i] <= dist[v[1]] + j: continue # 最小距離を更新できない場合
        dist[i] = dist[v[1]] + j
        heappush(q, (dist[i], i)) # 距離・ノード
print(dist[-1])
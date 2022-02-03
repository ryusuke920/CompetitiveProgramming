from collections import deque
from sys import setrecursionlimit
import sys

setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def search_num_child(now: int) -> int:
    """0を根とした木において、頂点now以下の頂点数（頂点nowとその子の数）をdfsで求める"""
    if num_child[now]: return num_child[now]
    num_child[now] = 1 # 自分自身
    for nxt in g[now]:
        if num_child[nxt]: continue
        num_child[now] += search_num_child(nxt)

    return num_child[now]

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    x, y = map(int,input().split())
    g[x - 1].append(y - 1)
    g[y - 1].append(x - 1)

# num_child[i] := 頂点0を根としたiの部分木の大きさ（iを含む）
num_child = [0] * n
search_num_child(0)
dis_from_zero = sum(num_child) - n

# 0を根としてbfsで高さが低い頂点から(0に近い頂点から)ansを求めていく
ans = [dis_from_zero] * n
seen = [0] * n
q = deque()
q.append((0, -1))
while q:
    now, parents = q.popleft()
    seen[now] = 1

    if now:
        res = ans[parents]
        # 移動後は頂点の子のノードは距離が減る
        res -= num_child[now]
        # 移動後の頂点の親ノードは距離が増える
        res += n - num_child[now]
        ans[now] = res
    
    for nxt in g[now]:
        if seen[nxt]: continue
        q.append((nxt, now))

print(*ans, sep="\n")
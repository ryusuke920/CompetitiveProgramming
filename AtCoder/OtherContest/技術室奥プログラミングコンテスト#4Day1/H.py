from heapq import heappush, heappop
import sys
input = sys.stdin.readline
n, m, K = map(int,input().split())
t = [0] * n
for i in range(n - 2):
    t[i + 1] = int(input())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b, c, d = map(int,input().split())
    if t[a - 1] >= K and t[b - 1] >= K: continue
    elif t[a - 1] >= K:
        graph[b - 1].append((a - 1, c, d, t[a - 1])) # ノード・コスト・周期・乗り換えコスト
    elif t[b - 1] >= K:
        graph[a - 1].append((b - 1, c, d, t[b - 1])) # ノード・コスト・周期・乗り換えコスト
    else:
        graph[a - 1].append((b - 1, c, d, t[b - 1])) # ノード・コスト・周期・乗り換えコスト
        graph[b - 1].append((a - 1, c, d, t[a - 1])) # ノード・コスト・周期・乗り換えコスト

dist = [10 ** 18] * n
if len(graph[0]) == 0:
    exit(print(-1))
else:
    q = [(0, 0)] # 総コスト・ノード
    dist[0] = 0

while q:
    v2, v1 = heappop(q) # 今までのコスト・ノード
    for i, j, k, l in graph[v1]: # 先のノード・必要なコスト・周期・乗り換えコスト
        if dist[i] <= v2: continue
        if dist[i] <= v2 + j + l + ((k - v2 % k) % k): continue
        dist[i] = v2 + j + l + ((k - v2 % k) % k) # （今までの総距離 + 今回必要なコスト + 乗り換えコスト + 待ち時間）
        heappush(q, (dist[i], i))

if dist[-1] <= K:
    print(dist[-1])
else:
    print(-1)
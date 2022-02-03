from heapq import heappush, heappop
import sys
input = sys.stdin.readline
n, m, x, y = map(int,input().split())
(x, y) = (x - 1, y - 1)
graph = [[] for _ in range(n)]
for i in range(m):
    (a, b, t, k) = map(int,input().split())
    graph[a - 1].append([b - 1, t, k])
    graph[b - 1].append([a - 1, t, k])

dist = [10 ** 18] * n
check = [False] * n
if len(graph[x]) == 0:
    exit(print(-1))
else:
    q = [(0, x)]
dist[x] = 0
while q:
    v1, v2 = heappop(q) # 今いる距離・ノード
    for i, j, k in graph[v2]: # 先のノード・コスト・周期
        if k - v1 % k == 0: # ちょうど発車できる時
            if dist[i] <= j + v1: continue
            dist[i] = j + v1
            heappush(q, [dist[i], i])
        else: # 待たなきゃいけない時 (k - v1）だけ待たなきゃいけない）
            if dist[i] <= j + v1 + (k - v1) % k: continue
            dist[i] = j + v1 + (k - v1) % k # （今までの総距離 + 今回の必要なコスト + 待ち時間）
            heappush(q, [dist[i], i])

if dist[y] == 10 ** 18:
    print(-1)
else:
    print(dist[y])
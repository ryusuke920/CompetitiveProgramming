from collections import deque
n = int(input())
graph = [[] for _ in range(n)] # 隣接リスト（無向グラフであれば隣接行列）
for i in range(n):
    a = list(map(int,input().split()))
    for j in range(a[1]):
        graph[a[0] - 1].append(a[j + 2] - 1)

dist = [-1] * n
dist[0] = 0 # 頂点０→０の距離は当然０
q = deque()
q.append(0)
while q:
    v = q.popleft()
    for i in graph[v]:
        if dist[i] == -1: # まだ行ってない所であれば今いる頂点 + 1をした距離が最小値となる
            dist[i] = dist[v] + 1
            q.append(i) # qに距離を記録した頂点を追加する

for i in range(n):
    print(i + 1, dist[i])
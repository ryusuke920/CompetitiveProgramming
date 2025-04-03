from heapq import heappush, heappop
from collections import deque

import sys
input = sys.stdin.readline

def dijkstra(s: int, graph: list, n: int) -> list:
    dist = [10 ** 10] * n
    check = [False] * n
    dist[s] = 0
    q = [(0, s)]
    while q:
        v = heappop(q)[1]
        if check[v]: continue
        check[v] = True
        for i, j in graph[v]:
            if check[i] != False: continue
            if dist[i] < dist[v] + j: continue
            dist[i] = dist[v] + j
            heappush(q, (dist[i], i))

    return dist

def bfs(g: list, s: int, n: int) -> list:
    q = deque()
    q.append(s)
    INF = 10 ** 10
    dist = [INF] * n
    dist[s] = 0
    while q:
        v = q.popleft()
        for i in g[v]:
            if dist[i] != INF: continue
            dist[i] = dist[v] + 1
            q.append(i)
    
    return dist

def main():
    n, k = map(int, input().split())
    cr = [tuple(map(int ,input().split())) for _ in range(n)]
    xy = [list(map(int, input().split())) for _ in range(k)]

    g = [[] for _ in range(n)]
    for i in range(k):
        xy[i][0] -= 1
        xy[i][1] -= 1
        g[xy[i][0]].append(xy[i][1])
        g[xy[i][1]].append(xy[i][0])

    dist = [bfs(g, i, n) for i in range(n)]

    g = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dist[i][j] <= cr[i][1]:
                g[i].append((j, cr[i][0]))

    print(dijkstra(0, g, n)[n - 1])

if __name__ == "__main__":
    main()
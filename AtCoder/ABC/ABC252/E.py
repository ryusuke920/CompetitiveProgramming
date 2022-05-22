from heapq import heappop, heappush

def main():
    INF = 10 ** 18

    n, m = map(int, input().split())

    g = [[] for _ in range(n)]
    for i in range(m):
        x, y, cost = map(int,input().split())
        x -= 1
        y -= 1
        g[x].append((i, y, cost))
        g[y].append((i, x, cost))

    dist = [INF] * n
    dist[0] = 0
    q = [(0, 0)]
    edge = []
    while q:
        pre = heappop(q)[1]
        for num, nxt, cost in g[pre]:
            if dist[nxt] < dist[pre] + cost: continue
            dist[nxt] = dist[pre] + cost
            edge.append(num + 1)
            heappush(q, (dist[nxt], nxt))
 
    print(*edge)


if __name__ == '__main__':
    main()
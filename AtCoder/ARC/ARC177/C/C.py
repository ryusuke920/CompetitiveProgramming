from heapq import heapify, heappop, heappush

def dist(sx: int, sy: int, num: int):
    dist = [[INF] * N for _ in range(N)]
    q = [(0, (sx, sy))]
    heapify(q)
    dist[sx][sy] = 0

    while q:
        _, (x, y) = heappop(q)
        for dy, dx in d:
            ny = y + dy
            nx = x + dx
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            cost = 1 if g[nx][ny] != num else 0
            if dist[nx][ny] > dist[x][y] + cost:
                dist[nx][ny] = dist[x][y] + cost
                heappush(q, (dist[nx][ny], (nx, ny)))
    return dist

def main() -> None:
    global N, g, d, INF
    N = int(input())
    g = [input() for _ in range(N)]
    d = ((1, 0), (-1, 0), (0, 1), (0, -1))
    INF = 10**18
    red = dist(0, 0, 'R') # 上
    blue = dist(0, N - 1, 'B') # 下
    ans = red[N - 1][N - 1] + blue[N - 1][0]
    print(ans)

if __name__ == "__main__":
    main()
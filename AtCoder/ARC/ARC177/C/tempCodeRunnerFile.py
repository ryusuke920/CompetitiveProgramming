import heapq

N = int(input())
G = [input() for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def calc_distance(sx, sy, ignore):
    dist = [[1e9] * N for _ in range(N)]
    heap = [(0, (sx, sy))]
    dist[sx][sy] = 0

    while heap:
        cur, (x, y) = heapq.heappop(heap)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                cost = 1 if G[nx][ny] != ignore else 0
                if dist[nx][ny] > dist[x][y] + cost:
                    dist[nx][ny] = dist[x][y] + cost
                    heapq.heappush(heap, (dist[nx][ny], (nx, ny)))
    return dist

def solve():
    Rdist = calc_distance(0, 0, 'R')
    Bdist = calc_distance(0, N - 1, 'B')
    ans = Rdist[N - 1][N - 1] + Bdist[N - 1][0]
    print(ans)

solve()
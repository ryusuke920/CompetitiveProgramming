from collections import deque

def main() -> None:
    h, w, t = map(int, input().split())
    a = [input() for _ in range(h)]

    n = 2
    for i in range(h):
        for j in range(w):
            if a[i][j] == "o":
                n += 1
    x, y = [0] * n, [0] * n
    oyatu_grid = [-1] * (h * w) # o の場所特定のための配列

    ind = 1
    for i in range(h):
        for j in range(w):
            if a[i][j] == "S":
                y[0], x[0] = i, j
                oyatu_grid[i * w + j] = 0
            if a[i][j] == "G":
                y[n - 1], x[n - 1] = i, j
                oyatu_grid[i * w + j] = n - 1
            if a[i][j] == "o":
                y[ind], x[ind] = i, j
                oyatu_grid[i * w + j] = ind
                ind += 1

    #print(f"{y=}")
    #print(f"{x=}")

    INF = 1 << 60
    dist = [INF] * (n**2)
    d = ((1, 0), (0, 1), (-1, 0), (0, -1))
    for i in range(n):
        q = deque()
        q.append(y[i] * w + x[i])
        dist_ = [INF] * (h * w) # 全てのマスのリスト
        dist_[y[i] * w + x[i]] = 0
        dist[i * n + i] = 0
        while q:
            num = q.popleft()
            vy, vx = num // w, num % w
            for dy, dx in d:
                ny = vy + dy
                nx = vx + dx
                if not (0 <= ny < h and 0 <= nx < w):
                    continue
                if dist_[ny * w + nx] != INF:
                    continue
                if a[ny][nx] == "#":
                    continue
                #print(h, w, vy, vx)
                dist_[ny * w + nx] = dist_[vy * w + vx] + 1
                if a[ny][nx] == "S" or a[ny][nx] == "G" or a[ny][nx] == "o":
                    dist[i * n + oyatu_grid[ny * w + nx]] = dist_[ny * w + nx]
                q.append(ny * w + nx)

    #for i in range(n):print(dist[i*n:(i + 1)*n])
    # dp[i][j] := 頂点の集合 2^i において、最後に訪れたマスが j である時の移動距離の最小値
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0
    for s in range(1 << n):
        # u -> v
        for u in range(n):
            if (s >> u) & 1:
                for v in range(n):        
                    if not (s >> v) & 1:
                        l = s | 1 << v
                        if dp[l][v] > dp[s][u] + dist[u * n + v]:
                            dp[l][v] = dp[s][u] + dist[u * n + v]
    #print(*dp,sep="\n")
    ans = -1
    for i in range(2**n):
        if dp[i][n - 1] <= t:
            cnt = str(bin(i)[2:]).count("1") - 2
            ans = max(ans, cnt)
    #print(*dp, sep="\n")
    print(ans)


if __name__ == "__main__":
    main()
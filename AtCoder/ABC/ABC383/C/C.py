from heapq import heapify, heappop, heappush

def main() -> None:
    H, W, D = map(int, input().split())
    S = [input() for _ in range(H)]
    grid = [[-1]*W for _ in range(H)]
    q = []
    heapify(q)
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            if S[i][j] == "H":
                grid[i][j] = D
                heappush(q, (-D, i, j))
    
    d = ((0, 1), (0, -1), (1, 0), (-1, 0))
    while q:
        cnt, vy, vx = heappop(q)
        cnt *= -1
        for dy, dx in d:
            ny = vy + dy
            nx = vx + dx
            if not (0 <= ny < H and 0 <= nx < W):
                continue
            if S[ny][nx] == "#":
                continue
            if grid[ny][nx] < cnt - 1:
                grid[ny][nx] = cnt - 1
                heappush(q, (-(cnt - 1), ny, nx))
    
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += grid[i][j] >= 0
    print(ans)


if __name__ == "__main__":
    main()
from collections import deque

def main() -> None:
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    A, B, C, D = map(lambda x: int(x) - 1, input().split())
    d2 = ((0, 1), (0, -1), (1, 0), (-1, 0), (0, 2), (0, -2), (2, 0), (-2, 0))

    grid = [[-1]*W for _ in range(H)]
    grid[A][B] = 0

    q = deque()
    q.appendleft((A, B))
    while q:
        vy, vx = q.popleft()
        for dy, dx in d2:
            ny = vy + dy
            nx = vx + dx
            if not (0 <= ny < H and 0 <= nx < W):
                continue
            if grid[ny][nx] != -1:
                    continue
            if S[ny][nx] == "#":
                grid[ny][nx] = grid[vy][vx] + 1
                q.append((ny, nx))
            else:
                if abs(dy) + abs(dx) >= 2:
                    continue
                grid[ny][nx] = grid[vy][vx]
                q.appendleft((ny, nx))
    print(grid[C][D])


if __name__ == "__main__":
    main()

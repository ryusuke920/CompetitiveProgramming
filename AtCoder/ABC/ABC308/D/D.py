from collections import deque

def main() -> None:
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]

    q = deque()
    dist = [[[False] * 5 for _ in range(1000)] for _ in range(1000)]
    if s[0][0] == "s":
        q.append((0, 0, 0))
        dist[0][0][0] = True
    else:
        exit(print("No"))
    
    d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while q:
        vy, vx, num = q.popleft()
        for dy, dx in d:
            ny = vy + dy
            nx = vx + dx
            ind = (num + 1) % 5
            if not (0 <= ny < h and 0 <= nx < w):
                continue
            if "snuke"[ind] == s[ny][nx] and dist[ny][nx][ind] == 0:
                q.append((ny, nx, ind))
                dist[ny][nx][ind] = 1
    
    ans = 0
    for i in range(5):
        ans += dist[h - 1][w - 1][i]
    
    print("Yes") if ans else print("No")


if __name__ == "__main__":
    main()
from collections import deque
def dfs(y, x):
    d = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    q = deque()
    q.append([y, x])
    while q:
        dy, dx = q.popleft()
        c[dy][dx] = 0
        for i, j in d:
            if 0 <= dy + i <= h - 1 and 0 <= dx + j <= w - 1:
                if c[dy + i][dx + j] == 1:
                    c[dy + i][dx + j] = 0
                    q.append([dy + i, dx + j])

while True:
    w, h = map(int,input().split())
    if (w, h) == (0, 0):
        exit()
    c = [list(map(int,input().split())) for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if c[i][j] == 1:
                ans += 1
                dfs(i, j)
    print(ans)
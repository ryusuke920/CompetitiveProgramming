import sys
input = sys.stdin.readline

h, w, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
c = list(map(int, input().split()))

bool = True
d = ((1, 0), (-1, 0), (0, 1), (0, -1))
for i in range(h):
    for j in range(w):
        for dy, dx in d:
            y = i + dy
            x = j + dx
            if not (0 <= y < h and 0 <= x < w):
                continue
            if a[i][j] == a[y][x]:
                continue
            if c[a[i][j] - 1] == c[a[y][x] - 1]:
                bool = False
                break

print('Yes') if bool else print('No')
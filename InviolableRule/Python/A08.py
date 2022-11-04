h, w = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(h)]

s = [[0] * (w + 1) for _ in range(h + 1)]
for i in range(h):
    for j in range(w):
        s[i + 1][j + 1] += s[i][j + 1] + s[i + 1][j] - s[i][j] + x[i][j]

q = int(input())
for _ in range(q):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    print(s[c][d] - s[c][b] - s[a][d] + s[a][b])
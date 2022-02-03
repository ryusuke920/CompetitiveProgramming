h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

b = [[0] * h for _ in range(w)]

for i in range(w):
    for j in range(h):
        b[i][j] = a[j][i]

for i in b:
    print(*i)
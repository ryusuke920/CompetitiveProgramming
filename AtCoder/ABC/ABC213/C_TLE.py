h, w, n = map(int,input().split())
grid = [[-1] * w for _ in range(h)]
for i in range(n):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    grid[a][b] = i + 1

grid_2 = []
for i in range(h):
    bool = False
    col = []
    for j in range(w):
        if grid[i][j] != -1:
            bool = True
        col.append(grid[i][j]) 

    if bool:
        grid_2.append(col) 

h = len(grid_2)
w = len(grid_2[0])

ans = [[] for _ in range(h)]

for i in range(w):
    bool = False
    col = []
    for j in range(h):
        if grid_2[j][i] != -1:
            bool = True
        col.append(grid_2[j][i])
    
    if bool:
        for j in range(h):
            ans[j].append(grid_2[j][i])

h = len(ans)
w = len(ans[0])

num = [(0, 0) for _ in range(n)]
num[0] = (1, 1)
for i in range(h):
    for j in range(w):
        if ans[i][j] != -1:
            num[ans[i][j] - 1] = (i + 1, j + 1)

for i in range(len(num)):
    print(*num[i])
h, w = map(int,input().split())
grid = []
for _ in range(h):
    g = list(input())
    if "#" not in g: continue
    grid.append(g)

h = len(grid)
ans = [[] for _ in range(h)]
for i in range(w):
    count = 0
    for j in range(h):
        if grid[j][i] == "#":
            count += 1
    if count == 0: continue
    for j in range(h):
        ans[j].append(grid[j][i])

for i in range(h):
    print(*ans[i], sep = "")
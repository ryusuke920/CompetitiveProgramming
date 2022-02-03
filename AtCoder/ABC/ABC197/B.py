h, w, y, x = map(int,input().split())
grid = []
for i in range(h):
    grid.append(list(input()))
ans = 1
now = -1
Bool = True
while True:
    if not (0 <= y - 1 + now <= h - 1):
        break
    if grid[y - 1 + now][x - 1] == "." and Bool == True:
        ans += 1
    else:
        Bool = False
    now -=1
now = 1
Bool = True
while True:
    if not (0 <= y - 1 + now <= h - 1):
        break
    if grid[y - 1 + now][x - 1] == "." and Bool == True:
        ans += 1
    else:
        Bool = False
    now += 1
now = -1
Bool = True
while True:
    if not (0 <= x - 1 + now <= w - 1):
        break
    if grid[y - 1][x - 1 + now] == "." and Bool == True:
        ans += 1
    else:
        Bool = False
    now -=1
now = 1
Bool = True
while True:
    if not (0 <= x - 1 + now <= w - 1):
        break
    if grid[y - 1][x - 1 + now] == "." and Bool == True:
        ans += 1
    else:
        Bool = False
    now += 1
print(ans)
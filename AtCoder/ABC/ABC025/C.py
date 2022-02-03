from itertools import product

b = [list(map(int, input().split())) for _ in range(2)]
c = [list(map(int, input().split())) for _ in range(3)]

ans_1, ans_2 = 0, 10 ** 18

for i in product([0, 1], repeat=9):
    takahashi, naoko = 0, 0
    grid = [[-1] * 3 for _ in range(3)]
    for j in range(9):
        y, x = j // 3, j % 3
        if i[j] == 1:
            grid[y][x] = 1
        elif i[j] == 0:
            grid[y][x] = 0
    
    for h in range(2):
        for w in range(3):
            if grid[h][w] == grid[h + 1][w]:
                takahashi += b[h][w]
            else:
                naoko += b[h][w]
    
    for h in range(3):
        for w in range(2):
            if grid[h][w] == grid[h][w + 1]:
                takahashi += c[h][w]
            else:
                naoko += c[h][w]
    
    if abs(ans_1 - ans_2) > abs(takahashi - naoko):
        ans_1 = takahashi
        ans_2 = naoko

print(ans_1)
print(ans_2)
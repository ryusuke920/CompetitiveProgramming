n = int(input())
m = int(input())

grid = [[0] * (n) for _ in range(m)] # 入力した値を打ち込む場所
d = [[1, 0], [-1, 0], [0, 1], [0, -1]] # 変化量[y, x]
for i in range(m):
    l = list(map(int,input().split()))
    for j in range(n):
        grid[i][j] = l[j]

def dfs(y, x, num):
    cnt = num
    check[y][x] = True
    for i, j in d:
        if not (0 <= y + i <= m - 1 and 0 <= x + j <= n - 1): continue # 範囲外なら調べない
        if check[y + i][x + j] == True: continue # 既にチェック済みの場所なら調べない
        if grid[y + i][x + j] == 0: continue # 薄氷でなければ調べない
        cnt = max(cnt, dfs(y + i, x + j, num + 1))
    check[y][x] = False
    return cnt

ans = 0 # 答え
for i in range(m):
    for j in range(n):
        if grid[i][j] == 1:
            check = [[False] * n for _ in range(m)]
            ans = max(ans, dfs(i, j, 1))
print(ans)
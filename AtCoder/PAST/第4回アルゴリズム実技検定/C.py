n,m = map(int,input().split())
s = []
for i in range(n):
    x = list(input())
    s.append(x)
ans = [[0]*m for _ in range(n)]
d = [[-1, -1], [-1, 0], [-1, 1], [0 , -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
for i in range(n):
    for j in range(m):
        for k in range(9):
            if s[i][j] == "#":
                if (i + d[k][0] >= 0) and (i + d[k][0] < n) and (j + d[k][1] >= 0) and (j + d[k][1] < m):
                    ans[i + d[k][0]][j + d[k][1]] += 1
for i in range(n):
    print(*ans[i], sep = "")
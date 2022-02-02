n,m = map(int,input().split())
amatrix = [list(map(int,input().split())) for _ in range(n)]
bmatrix = [int(input()) for _ in range(m)]
for i in range(n):
    ans = 0
    for j in range(m):
        ans += amatrix[i][j] * bmatrix[j]
    print(ans)
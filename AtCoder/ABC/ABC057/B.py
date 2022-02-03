n,m = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(n)]
cd = [list(map(int,input().split())) for _ in range(m)]
ans = [0]*n
for i in range(n):
    count = 10**9
    for j in range(m):
        ch = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
        if ch < count:
            ans[i] = j+1
            count = ch
    print(ans[i])
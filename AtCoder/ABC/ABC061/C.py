n,k = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(n)]
ab.sort()
cnt = 0
for i in range(n):
    cnt += ab[i][1]
    if cnt >= k:
        print(ab[i][0])
        exit()
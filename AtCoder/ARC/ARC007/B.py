n,m = map(int,input().split())
num = 0
d = [int(input()) for _ in range(m)]
cd = [i+1 for i in range(n)]
for i in range(m):
    for j in range(n):
        if d[i] == cd[j]:
            tmp = num
            num = cd[j]
            cd[j] = tmp
            break
for i in range(n):
    print(cd[i])
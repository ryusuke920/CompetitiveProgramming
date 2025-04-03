#2020/11/5
n,m = map(int,input().split())
a = [[] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int,input().split()))
ans = cnt = 0
score = [0]*n
for i in range(m-1):
    for j in range(i+1,m):
        for k in range(n):
            score[k] = max(a[k][i], a[k][j])
        ans = max(ans, sum(score))
print(ans)
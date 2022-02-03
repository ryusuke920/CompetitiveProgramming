b = list(map(str, input().split()))
n = int(input()) 
a = [int(input()) for _ in range(n)]
ans = []
for i in range(n):
    x = str(a[i])[::-1]
    num = 0
    for j in range(len(x)):
        cnt = b.index(x[j])
        num += pow(10, j) * cnt
    ans.append([num, int(x[::-1])])

ans.sort()
for i in range(n):
    print(ans[i][1])
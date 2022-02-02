h,w = map(int,input().split())
ans = [list(map(int,input().split())) for _ in range(h)]

for i in range(h):
    num = 0
    for j in range(w):
        num += ans[i][j]
    ans[i].append(num)

x = []
for i in range(w):
    num = 0
    for j in range(h):
        num += ans[j][i]
    x.append(num)

for i in range(h):
    print(*ans[i])

x.append(sum(x))
print(*x)
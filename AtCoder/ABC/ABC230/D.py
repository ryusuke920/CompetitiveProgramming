n, d = map(int,input().split())
lr = [list(map(int,input().split())) for _ in range(n)]

lr.sort(key = lambda x: (x[1], x[0]))
ans, ma = 0, 0

for i in range(n):
    l, r = lr[i]
    if ma < l:
        ans += 1
        ma = r + d - 1

print(ans)
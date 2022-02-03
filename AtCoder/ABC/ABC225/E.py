n = int(input())
xy = [list(map(int,input().split())) for _ in range(n)]
xy.sort(key = lambda x: x[0], reverse=True)
ans = 1
print(*xy, sep='\n')
now = xy[0][0]
for i in range(1, n):
    if now < xy[i][0]:
        ans += 1
    now = xy[i][0]

print(ans)
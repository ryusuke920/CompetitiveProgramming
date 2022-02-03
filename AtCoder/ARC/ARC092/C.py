n = int(input())
ab = [list(map(int,input().split())) for _ in range(n)]
cd = [list(map(int,input().split())) for _ in range(n)]

ab.sort(key=lambda x: x[1])
cd.sort(key=lambda x: x[0])

ans = 0
for c, d in cd:
    xs = [x for x in ab if x[0] < c and x[1] < d]
    if xs:
        ab.remove(xs[-1])
        ans += 1
print(ans)
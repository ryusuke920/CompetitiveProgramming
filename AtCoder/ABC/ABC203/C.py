n, k = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(n)]
ans = cnt = 0
ab.sort(key = lambda x: x[0])
now = 0
x = k
ans = 0
for i in range(n):
    if i == 0:
        cost = ab[i][0]
    else:
        cost = ab[i][0] - ab[i - 1][0]
    if k- cost < 0:
        exit(print(now + k))
    k -= cost
    k += ab[i][1]
    ans += ab[i][1]
    now = ab[i][0]
    #print(i,ans,k,now)
#print(ans)
print(ans + x)
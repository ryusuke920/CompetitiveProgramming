t,n = map(int,input().split())
tm = [[0,0,0] for _ in range(n)]
for i in range(n):
    a,b = map(int,input().split())
    tm[i][0] = a
    tm[i][1] = b
for i in range(n):
    tm[i][2] = tm[i][1] / tm[i][0]
tm.sort(key = lambda x: x[2], reverse = True)
print(tm)
ans = 0
time = 0
for i in range(n):
    if time + tm[i][0] <= t:
        ans += tm[i][1]
        time += tm[i][0]
    print(i,ans,time)
print(ans)
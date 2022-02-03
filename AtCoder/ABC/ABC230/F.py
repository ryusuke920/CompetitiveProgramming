n, d = map(int,input().split())
lr = [list(map(int,input().split())) for _ in range(n)]
lr.sort(key = lambda x: (x[0], x[1]))
ans = 0
now = lr[0][1]
cnt = 0
for i in range(1, n):
    if lr[i][0] - now + 1 < 0:
        ans += 1
        now = lr[i][1]
    else:
        cnt = max(0, lr[i][0] - now + 1)
        if cnt >= d:
            ans += 1
            cnt = 0
            now = lr[i][1]
    print(i,ans,cnt,now)

print(ans)
print(ans) if cnt == 0 else print(ans + 1)
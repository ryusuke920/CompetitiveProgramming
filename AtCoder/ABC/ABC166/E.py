n = int(input())
a = list(map(int,input().split()))
ans = 0
cnt = {}
for i in range(n):
    if a[i]+i in cnt:
        cnt[a[i]+i] += 1
    else:
        cnt[a[i]+i] = 1
    if i-a[i] in cnt:
        ans += cnt[i-a[i]]
print(ans)
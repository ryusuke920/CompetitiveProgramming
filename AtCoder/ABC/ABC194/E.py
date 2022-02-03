n, m = map(int,input().split())
a = list(map(int,input().split()))
cnt = [0] * (n + 1)
for i in range(m):
    cnt[a[i]] += 1

ans = n
for i in range(n + 1):
    if cnt[i] == 0:
        ans = i
        break

for i in range(n - m):
    cnt[a[i]] -= 1
    cnt[a[m + i]] += 1
    if cnt[a[i]] == 0:
        ans = min(ans, a[i])
print(ans)
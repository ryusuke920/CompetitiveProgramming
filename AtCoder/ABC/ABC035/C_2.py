n, q = map(int, input().split())

cnt = [0] * (n + 1)
for _ in range(q):
    l, r = map(int, input().split())
    cnt[l - 1] += 1
    cnt[r] -= 1

for i in range(n):
    cnt[i + 1] += cnt[i]

ans = []
for i in cnt:
    if i % 2:
        ans.append(1)
    else:
        ans.append(0)

print(*ans[:n], sep='')
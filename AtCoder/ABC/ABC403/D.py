from collections import Counter, defaultdict
N, D = map(int, input().split())
A = list(map(int, input().split()))

cnt = Counter(A)
if D == 0:
    exit(print(N - len(cnt)))

d = defaultdict(list)
for i in cnt:
    d[i % D].append(i)

ans = 0
for v in d.values():
    v.sort()
    dp1, dp2 = 0, 0
    flag = None
    for i in v:
        num = cnt[i]
        if flag is not None and i == flag + D:
            tmp = max(dp1, dp2 + num)
        else:
            tmp = dp1 + num
        dp2, dp1 = dp1, tmp
        flag = i
    ans += dp1

print(N - ans)

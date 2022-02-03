n, k = map(int,input().split())
v = list(map(int,input().split()))
ans = 0
if 2 * n <= k: # この条件を満たすときはプラスのものだけ全部取り込める
    for i in range(n):
            ans += max(0, v[i])
else:
    for i in range(min(n, k) + 1):
        for j in range(min(n, k) + 1):
            a, b, c, cnt = [], [], [], 0
            for l in range(i):
                if cnt > min(n ,k): continue
                cnt += 1
                a.append(v[l])
            for l in range(max(0, min(min(n, k) - i, j))):
                if cnt > min(n, k): continue
                cnt += 1
                b.append(v[-1 - l])
            num = max(0, min(n, k) - (i + j)) # 取り除くことのできる回数

            for l in range(len(a)):
                c.append(a[l])
            for l in range(len(b)):
                c.append(b[l])
            c.sort()
            tmp = sum(c)
            ans = max(ans, tmp)
            for l in range(min(num, len(c))):
                tmp -= c[l]
                ans = max(ans ,tmp)
print(ans)
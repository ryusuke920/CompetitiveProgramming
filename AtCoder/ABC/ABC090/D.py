n, k = map(int,input().split())
ans = 0
if k == 0:
    print(n ** 2)
else:
    for b in range(k + 1, n + 1):
        q = n // b
        ans += q * (b - k) + max(n % b + 1 - k, 0)
    print(ans)
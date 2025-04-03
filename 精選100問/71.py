n, q = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

mod = 10 ** 9 + 7
dist = [0] * (n - 1) # dist[i] := iからi + 1への距離
for i in range(n - 1):
    dist[i] = pow(a[i], a[i + 1], mod)

# 距離の累積和を取る
for i in range(n - 2):
    dist[i + 1] += dist[i]

ans = dist[c[0] - 2]
for i in range(q - 1):
    x, y = c[i], c[i + 1]
    if x > y: x, y = y, x
    ans += dist[y - 2] - dist[x - 2]
    ans %= mod
print(dist)
ans += dist[c[-1] - 2]
print(ans % mod)
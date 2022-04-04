n, k, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    while k > 0:
        cnt = a[i] // x
        if cnt == 0: break
        if k - cnt >= 0:
            a[i] -= x * cnt
            k -= cnt
        else:
            a[i] -= x * k
            k = 0

a.sort(reverse=True)
for i in range(min(k, n)):
    a[i] = 0

print(sum(a))
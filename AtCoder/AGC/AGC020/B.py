k = int(input())
a = list(map(int,input().split()))[::-1]

l, r = 2, 2

if a[0] > 2:
    exit(print(-1))

for i in range(1, k):
    l += (a[i] - l % a[i]) % a[i]
    r += a[i - 1] - 1
    r -= r % a[i]

    if l > r:
        exit(print(-1))

print(l, r + a[-1] - 1)
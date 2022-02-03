n, l, w = map(int, input().split())
a = list(map(int, input().split()))

left = 0
ans = 0
for right in range(n):
    ans += (a[right] - left + (w - 1)) // w
    left = a[right] + w

ans += (l - left + (w - 1)) // w

print(ans)
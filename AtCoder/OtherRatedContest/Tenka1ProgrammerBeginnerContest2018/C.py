n = int(input())
a = [int(input()) for _ in range(n)]
a.sort()

odd, even = 0, 0
if n % 2 == 0: # even
    x = 2 * sum(a[n // 2:]) - a[n // 2]
    y = -2 * sum(a[:n // 2]) + a[n // 2 - 1]
    
    even = x + y
    ans = max(even, -even)
elif n % 2 == 1: # odd
    x = 2 * sum(a[n // 2:]) - (a[n // 2] + a[n // 2 + 1])
    y = -2 * sum(a[:n // 2])

    xx = 2 * sum(a[n // 2 + 1:])
    yy = -2 * sum(a[:n // 2 + 1]) + a[n // 2] + a[n // 2 - 1]
    odd = x + y
    ans = max(odd, -odd, xx + yy, -(xx + yy))

print(ans)
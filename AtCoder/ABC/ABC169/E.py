n = int(input())
a, b = [0] * n, [0] * n
for i in range(n):
    a[i], b[i] = map(int,input().split())
a.sort()
b.sort()

if n % 2 == 0:
    mid_a = (a[n // 2 - 1] + a[n // 2])
    mid_b = (b[n // 2 - 1] + b[n // 2])
    print(mid_b - mid_a + 1)
else:
    mid_a = a[n // 2]
    mid_b = b[n // 2]
    print(mid_b - mid_a + 1)
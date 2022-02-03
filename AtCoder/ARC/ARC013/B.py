c = int(input())
x = y = z = 0
for i in range(c):
    a = list(map(int,input().split()))
    a.sort()
    x = max(a[0], x)
    y = max(a[1], y)
    z = max(a[2], z)
print(x*y*z)
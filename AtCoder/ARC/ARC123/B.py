n = int(input())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())))
c = sorted(list(map(int,input().split())))

ans = x = y = z = 0
while True:
    if (x == n) or (y == n) or (z == n):
        exit(print(ans))
    if a[x] < b[y] < c[z]:
        ans += 1
        x += 1
        y += 1
        z += 1
    elif a[x] >= b[y] and a[x] >= c[z]:
        y += 1
        z += 1
    elif a[x] >= b[y]:
        y += 1
    elif a[x] >= c[z] or b[y] >= c[z]:
        z += 1
n = int(input())
#x, y = map(int,input().split())
a = list(map(int,input().split()))
ans = cnt = 0
a.sort()
if n % 2 == 0:
    mid = (a[n // 2] + a[n // 2 - 1]) / 2
else:
    mid = a[n // 2]

x = mid / 2 * n
y = sum(a)
z = 0

for i in range(n):
    z += min(a[i], mid)
    #print(i,a[i], mid, z)
print((x + y - z) / n)
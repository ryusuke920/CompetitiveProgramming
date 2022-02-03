n = int(input())
a = list(map(int,input().split()))
b = [0] * n
for i in range(n):
    b[i] = a[i]
b = b[::-1]
x = y = z = 0
for i in range(n - 1):
    x += (n - 1 - i) * (a[i] ** 2)
    #print(n-1-i,a[i])

wa = [0] * n
wa[0] = b[0]
for i in range(n - 1):
    wa[i + 1] += wa[i] + b[i + 1]
#print("wa = ",wa)
#print(b)

for i in range(n - 1):
    y -= 2 * a[i] * (wa[-2 - i])

for i in range(n  - 1):
    z += (i + 1) * (a[i + 1] ** 2)
print(x + y + z)
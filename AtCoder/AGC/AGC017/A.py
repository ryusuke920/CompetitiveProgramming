import math
n, p = map(int,input().split())
a = list(map(int,input().split()))
gu = 0
ans = 0
for i in range(n):
    if a[i]%2 == 0:
        gu += 1

if gu == n and p == 0:
    print(2 ** n)
elif gu == n and p == 1:
    print(0)
else:
    print(2 ** (n - 1))
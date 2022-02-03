a = list(map(int,input().split()))
cna = cnb = 0
a.sort()
x = a[2]-a[1]
y = a[1]-a[0]
if a[0]*a[1]*a[2]%2 != 0:
    print(0)
    exit()
while True:
    if x%2 == 0 and x != 0:
        cna += 1
        x //= 2
    else:
        break
while True:
    if y%2 == 0 and y != 0:
        cnb += 1
        y //= 2
    else:
        break
if cna == 0 and cnb == 0:
    print(-1)
else:
    print(min(cna,cnb))
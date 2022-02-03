a = list(map(int,input().split()))
a.sort()
dif = 2*a[2]-a[1]-a[0]
if dif%2 == 0:
    print(dif//2)
else:
    print(dif//2+2)
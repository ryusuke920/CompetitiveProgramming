a = list(map(int,input().split()))
n = int(input())
d = a[3]
s = min(a[2],a[1]*2,a[0]*4)
mi = min(s*2,d)
if n%2 == 0:
    if mi == s*2:
        print(n//2*2*s)
    else:
        print(n//2*d)
else:
    if mi == s*2:
        print(n*s)
    else:
        print(n//2*d+s)
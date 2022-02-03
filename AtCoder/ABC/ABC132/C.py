n = int(input())
d = list(map(int,input().split()))
d.sort()
if n%2 == 1:
    print(0)
else:
    print(d[n//2]-d[n//2-1])
n,m = map(int,input().split())
x = sorted(list(map(int,input().split())))
y = sorted([x[i+1]-x[i] for i in range(m-1)])
if n >= m:
    print(0)
else:
    print(sum(y[:m-n]))
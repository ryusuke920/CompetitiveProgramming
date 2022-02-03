n,m = map(int,input().split())
if n == 1 and m == 1:
    print(1)
elif n == 1:
    print(m-2)
elif m == 1:
    print(n-2)
else:
    print(max(n*m-(n*2+(m-2)*2),0))
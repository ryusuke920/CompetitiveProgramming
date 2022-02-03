k,a,b = map(int,input().split())
if b-a <= 2:
    print(k+1)
else:
    if (k-a+1)%2 == 0:
        print((k-a+1)//2*(b-a) + a)
    else:
        print((k-a+1)//2*(b-a) + a+1)
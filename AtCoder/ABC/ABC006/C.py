n,m = map(int,input().split())
if m < 2*n or m > 4*n:
    print(-1,-1,-1)
else:
    # a = 1
    for a in range(m//2+1):
        if (m-2*a)%4 == 0 and a + 0 + (m-2*a)//4 == n:
            exit(print(a,0,(m-2*a)//4))
    # b = 1
    for a in range((m-3)//2+1):
        if (m-2*a-3)%4 == 0 and a + 1 + (m-2*a)//4 == n:
            exit(print(a,1,(m-2*a-3)//4))
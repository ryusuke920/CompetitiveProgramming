a,r,n = map(int,input().split())
if r == 1:
    print(a)
else:
    for _ in range(n-1):
        a *= r
        if a > 10**9:
            print("large")
            exit()
    else:
        print(a)
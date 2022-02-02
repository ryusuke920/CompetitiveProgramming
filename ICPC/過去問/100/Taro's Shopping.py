while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    a = list(map(int,input().split()))
    a.sort(reverse = True)
    ans = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i]+a[j] >= ans and a[i]+a[j] <= m:
                ans = a[i]+a[j]
    if ans == 0:
        print("NONE")
    else:
        print(ans)
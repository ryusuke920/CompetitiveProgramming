while True:
    n = int(input())
    if n == 0:
        exit()
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        if sum(a)/n >= a[i]:
            ans += 1
    print(ans)
    ans = 0
while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    num = [0]*n
    ans = 0
    for i in range(n):
        if a[i] <= b[i]:
            num[i] = b[i] - a[i]
        else:
            num[i] = (m-a[i]) + b[i]
    ch = num[0]   
    for i in range(1, n): #１周回った方がいい説
        if abs(ch - num[i]) > abs(m + num[i] - ch):
            num[i] += m
    for i in range(n-1):
        if num[i+1] > num[i]:
            ans += num[i+1] - num[i]
    print(ans + ch)
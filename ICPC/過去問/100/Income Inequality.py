while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int,input().split()))
    cnt = 0
    ave = sum(a)/n
    for i in range(n):
        if ave >= a[i]:
            cnt += 1
    print(cnt)
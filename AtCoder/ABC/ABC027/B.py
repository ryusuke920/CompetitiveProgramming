n = int(input())
a = list(map(int,input().split()))
s = sum(a)
if  s%n == 0:
    count = 0
    for i in range(n-1):
        if a[i] != s//n:
            a[i+1] -= s//n - a[i]
            count += 1
    print(count)
else:
    print(-1)
n = int(input())
a = list(map(int,input().split()))
ans = 1
b = 0
for i in range(n):
    if a[i] == 0:
        b = 1
        print(0)
if b == 0:
    for i in range(n):
        ans *= a[i]
        if ans > 10**18:
            print(-1)
            break
    else:
        print(ans)
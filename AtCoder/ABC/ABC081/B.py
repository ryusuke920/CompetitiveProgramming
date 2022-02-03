n = int(input())
a = list(map(int,input().split()))
count = 0
ans = 10000
for i in range(n):
    while True:
        if a[i]%2 == 0:
            count += 1
            a[i] = a[i]//2
        else:
            ans = min(ans,count)
            count = 0
            break
print(ans)
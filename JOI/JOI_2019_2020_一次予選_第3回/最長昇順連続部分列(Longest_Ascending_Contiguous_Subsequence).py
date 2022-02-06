n = int(input())
a = list(map(int,input().split()))
ans = 1
for i in range(n-1):
    num = 0
    while a[i + num] <= a[i + 1 + num]:
        num += 1
        if i + num  + 1 == n:
            break
    ans = max(ans, num + 1)
print(ans)
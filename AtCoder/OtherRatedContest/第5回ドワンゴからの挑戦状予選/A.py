n = int(input())
a = list(map(int,input().split()))
ave = sum(a)/n
ans = abs(ave-a[0])
num = 0
for i in range(1,n):
    tmp = abs(ave-a[i])
    if tmp < ans:
        ans = tmp
        num = i
print(num)
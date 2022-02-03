n = int(input())
a = list(map(int,input().split()))
num = sum(a) - a[0]
x = a[0]
ans = num - x
for i in range(n-2):
    x += a[i+1]
    num -= a[i+1]
    ans = min(ans,abs(num-x))
print(ans)
n = int(input())
a = list(map(int,input().split()))
ans = 0
a = a[::-1]
for i in range(n):
    ans += a[i]*2**(i+1)
print(ans//2)
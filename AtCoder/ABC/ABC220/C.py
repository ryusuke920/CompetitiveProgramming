n = int(input())
a = list(map(int,input().split()))
x = int(input())
p = x // sum(a)
ans = p * n
num = sum(a) * p

for i in range(n):
    if num > x:
        exit(print(ans))
    ans += 1
    num += a[i]
print(ans)
n, t = map(int,input().split())
a = list(map(int,input().split()))
num = a[0]
for i in range(n - 1):
    x = a[i + 1]
    while num > x:
        x += t
    num = x
print(num)
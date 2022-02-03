n, k = map(int,input().split())
a = list(map(int,input().split()))

num = 0
for i in range(k):
    num += a[i]
print(num)

for i in range(n - k):
    num += a[i + k]
    num -= a[i]
    print(num)
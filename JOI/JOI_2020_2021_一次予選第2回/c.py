n = int(input())
a = list(map(int,input().split()))
x = y = 0
ma = max(a)
for i in range(n):
    if a[i] == ma:
        x = sum(a[:i])
print(x)
y = sum(a) - x - ma
print(y)
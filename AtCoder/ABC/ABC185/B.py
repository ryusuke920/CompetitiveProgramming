n, m, t = map(int,input().split())
num = n
x = 0
for i in range(m):
    a, b = map(int,input().split())
    n -= a - x
    if n <= 0:
        exit(print("No"))
    n = min(n + (b - a), num)
    x = b
n -= (t - x)
if n <= 0:
    exit(print("No"))
print("Yes")
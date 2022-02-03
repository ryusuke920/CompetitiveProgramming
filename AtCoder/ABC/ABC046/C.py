n = int(input())
a = b = 1
for i in range(n):
    x, y = map(int,input().split())
    num = max(-(-a // x), -(-b // y))
    a = x * num
    b = y * num
print(a + b)
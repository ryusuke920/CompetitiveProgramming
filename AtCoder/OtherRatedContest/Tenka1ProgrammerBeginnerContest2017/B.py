n = int(input())
num = 0
ans = 0
for i in range(n):
    a,b = map(int,input().split())
    if a >= num:
        num = a
        ans = b
print(num+ans)
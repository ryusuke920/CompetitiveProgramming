n = int(input())
a = [0]*n
b = [0]*n
x = y = 0
ans = 0
for i in range(n):
    a,b = map(int,input().split())
    x = max(0,a*(a-1)//2)
    y = b*(b+1)//2
    ans += y-x
ancnt = 0
print(ans)
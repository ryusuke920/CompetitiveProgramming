x,y,a,b = map(int,input().split())
ans = 0
y -= 1
while x*(a-1) < b and x*a <= y:
    x *= a
    ans += 1
ans += (y-x)//b
print(ans)
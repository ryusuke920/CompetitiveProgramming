w,a,b, = map(int,input().split())
ans = 0
if a <= b:
    ans = b - (w+a)
    if ans < 0:
        ans = 0
else:
    ans = a - (w+b)
    if ans < 0:
        ans = 0
print(ans)
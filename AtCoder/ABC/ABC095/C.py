a,b,c,x,y = map(int,input().split())
ab = c*2 #A,B１枚ずつ入手
if ab <= a+b:
    bab = min(x,y)*ab
    if x > y:
        bother = (max(x,y)-min(x,y))*a
    else:
        bother = (max(x,y)-min(x,y))*b
    ans = min(bab+bother,ab*max(x,y))
else:
    bab = 0
    bother = a*x + b*y
    ans = bab + bother
print(ans)
#2020/11/5
a,b,c,x,y = map(int,input().split())
money = 0
if a+b >= c*2:
    money += min(x, y)*c*2
    if x > y:
        money += (x-y)*min(c*2, a)
    else:
        money += (y-x)*min(c*2, b)
else:
    money += a*x
    money += b*y
print(money)
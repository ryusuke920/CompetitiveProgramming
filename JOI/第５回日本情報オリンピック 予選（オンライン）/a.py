n = int(input())
a = b = 0
for i in range(n):
    x,y = map(int,input().split())
    if x > y:
        a += x+y
    elif x == y:
        a += x
        b += y
    else:
        b += x+y
print(a,b)
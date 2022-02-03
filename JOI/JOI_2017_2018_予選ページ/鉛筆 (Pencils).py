import math
n,a,b,c,d = map(int,input().split())
x1 = math.ceil(n/a)*b
x2 = math.ceil(n/c)*d
if n%a == 0:
    x3 = n//a*b
else:
    x3 = n//a*b + math.ceil((n-n//a*a)/c)*d
if n%c == 0:
    x4 = n//c*d
else:
    x4 = n//c*d + math.ceil((n-n//c*c)/a)*b
print(x1,x2,x3,x4)
print(min(x1,x2,x3,x4))
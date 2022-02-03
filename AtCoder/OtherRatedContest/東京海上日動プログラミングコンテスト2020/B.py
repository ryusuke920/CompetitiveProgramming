a,v = map(int,input().split())
b,w = map(int,input().split())
t = int(input())
if a > b:
    A = a - v*t
    B = b - w*t
    if A <= B:
        print("YES")
    else:
        print("NO")
else:
    A = a + v*t
    B = b + w*t
    if A >= B:
        print("YES")
    else:
        print("NO")
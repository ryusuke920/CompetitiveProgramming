a,b,c = map(int,input().split())
d =[]
if a != b and b != c and c != a:
    print(3)
elif a == b == c:
    print(1)
else:
    print(2)
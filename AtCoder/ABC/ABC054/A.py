a,b = map(int,input().split())
if a>b and a!=1 and b!=1:
    print("Alice")
elif a<b and a!=1 and b!=1:
    print("Bob")
elif a==b:
    print("Draw")
elif a==1:
    print("Alice")
else:
    print("Bob")
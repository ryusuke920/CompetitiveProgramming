a,b = map(int,input().split())
if abs(a) == abs(b):
    print("Draw")
elif abs(a) > abs(b):
    print("Bug")
else:
    print("Ant")
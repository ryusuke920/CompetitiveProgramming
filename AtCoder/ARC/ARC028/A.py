n,a,b = map(int,input().split())
num = 1
while True:
    if num == 1:
        n -= a
        num = 0
    else:
        n -= b
        num = 1
    if n <= 0:
        break
if num == 1:
    print("Bug")
else:
    print("Ant")
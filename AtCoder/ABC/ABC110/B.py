n,m,X,Y = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
x.sort()
y.sort()
for i in range(X+1,Y+1,1):
    if i <= min(y) and i > max(x):
        print("No War")
        break
else:
    print("War")
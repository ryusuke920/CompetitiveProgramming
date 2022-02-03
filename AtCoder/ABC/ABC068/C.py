n,m = map(int,input().split())
leave = []
arrive = []
for i in range(m):
    a,b = map(int,input().split())
    if a == 1:
        leave.append(b)
    elif b == n:
        arrive.append(a)
if list(set(leave) & set(arrive)):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
x,n = map(int,input().split())
p = list(map(int,input().split()))
ans = 1000000
a = 0
if x not in p:
    a = 1
else:#xがpに入っていない場合
    for i in range(n):
        ch = abs(x-p[i])
        ans = min(ans,ch)
count = x-ans-1
if a == 1:
    print(x)
elif count not in p:
    print(count)
else:
    for j in range(ans,10000,1):
        if (x-j>=0) and x-j not in p:
            print(x-j)
            break
        elif x+j not in p:
            print(x+j)
            break
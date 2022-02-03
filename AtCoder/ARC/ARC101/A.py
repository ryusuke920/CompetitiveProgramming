n,k = map(int,input().split())
x = list(map(int,input().split()))
ans = 10**9
for i in range(n-k+1):
    if x[i]*x[i+k-1] < 0:
        ch = min(abs(x[i]), abs(x[i+k-1]))*2 + max(abs(x[i]), abs(x[i+k-1]))
    else:
        if x[i] == 0:
            ch = x[i+k-1]
        elif x[i+k-1] == 0:
            ch = -x[i+k-1]
        else:
            ch = max(abs(x[i]), abs(x[i+k-1]))
    ans = min(ans,ch)
print(ans)
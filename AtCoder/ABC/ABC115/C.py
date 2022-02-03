n,k = map(int,input().split())
h = [int(input()) for i in range(n)]
h.sort()
ans = 1000000001
for i in range(n-k+1):
    ch = h[i+k-1]-h[i]
    ans = min(ans,ch)
print(ans)
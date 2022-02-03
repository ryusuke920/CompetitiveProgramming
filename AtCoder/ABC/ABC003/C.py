n,k = map(int,input().split())
r = list(map(int,input().split()))
r.sort()
r = r[n-k:]
#print(r)
ans = 0
for i in range(k):
    ans = (ans+r[i])/2
print(ans)
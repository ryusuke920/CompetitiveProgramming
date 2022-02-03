n,k = map(int,input().split())
ans = 0
def multi(N,K):
    return max(0, min(K-1, 2*N-K+1))
for i in range(2,2*n+1):
    x = i
    ans += multi(n,x) * multi(n,x-k)
print(ans)
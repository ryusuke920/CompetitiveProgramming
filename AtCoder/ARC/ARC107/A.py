a,b,c = map(int,input().split())
mod = 998244353
print((a*(a+1)//2 * b*(b+1)//2 * c*(c+1)//2)%mod)
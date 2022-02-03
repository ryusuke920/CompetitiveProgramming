n,p=map(int,input().split())
print(pow(p-2,n-1,10**9+7)*(p-1)%(10**9+7))
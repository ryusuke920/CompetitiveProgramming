n,k = map(int,input().split())
rest = n%k
print(min(rest,k-rest))
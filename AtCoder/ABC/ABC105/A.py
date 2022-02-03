n,k = map(int,input().split())
if k >= n:
    print(k%n)
else:
    print(n%k)
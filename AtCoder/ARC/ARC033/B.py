n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = a+b
c = set(c)
print((n+m-len(c))/len(c))
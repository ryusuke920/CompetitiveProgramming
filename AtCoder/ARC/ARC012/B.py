n,a,b,l = map(int,input().split())
for i in range(n):
    l = l*b/a
print(round(l,10))
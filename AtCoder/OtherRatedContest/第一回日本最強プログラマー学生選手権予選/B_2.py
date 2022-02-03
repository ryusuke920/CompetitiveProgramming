n,k,*a=map(int,open(0).read().split())
x=0
y=0
for i in range(n):
    for j in range(n):
        if a[i]>a[j]:
            x+=1
            if i>j:y+=1
print((y*k+x*k*(k-1)//2)%(10**9+7))
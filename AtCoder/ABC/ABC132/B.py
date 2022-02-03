n = int(input())
count=0
p=list(map(int,input().split()))
for i in range(n-2):
    if (p[i]<p[i+1]<p[i+2]) or (p[i]>p[i+1]>p[i+2]):
        count+=1
print(count)
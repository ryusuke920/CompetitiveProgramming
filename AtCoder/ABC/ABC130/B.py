N,X = map(int,input().split())
L =list(map(int,input().split()))
dis=0
count=1
for i in range(N):
    dis+=L[i]
    if X>=dis:
        count+=1
print(count)
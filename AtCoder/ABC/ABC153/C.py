N,K=map(int,input().split())
H= list(map(int,input().split()))
count=0
H.sort()
for i in range(N-K):
    count+=H[i]
print(count)
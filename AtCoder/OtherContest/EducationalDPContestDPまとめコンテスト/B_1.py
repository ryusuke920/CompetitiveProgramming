n,k = map(int,input().split())
h = list(map(int,input().split()))
dp = [0]
for i in range(n-1):
    cnt = 10**9
    for j in range(k):
        if i-j < 0: continue
        cnt = min(dp[-1-j] + abs(h[i-j]-h[i+1]), cnt)
        #print("i =",i,"j =",j,"i-j =",i-j,"i+j =",i+j,"cnt =",cnt)
    dp += [cnt]
print(dp[-1])
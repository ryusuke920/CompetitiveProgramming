k,s = map(int,input().split())
count = 0
for i in range(k+1):
    for j in range(k+1):
        l = s-(i+j)
        if i+j+l == s and l >= 0 and l <= k and i <= k and j <= k:
            #print("解：",i,j,l)
            count += 1
print(count)
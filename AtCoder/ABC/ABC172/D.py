n = int(input())
ans = 0
num = [0]*n
for i in range(1,n+1):
    for j in range(i,n+1,i):
        num[j-1] += 1
for i in range(n):
    ans += (i+1)*num[i]
print(ans)
import math
k=int(input())
sum1=0
sum2=0
for a in range(1,k+1):
    for b in range(1,k+1):
        sum1=math.gcd(a,b)
        for c in range(1,k+1):
            sum2+=math.gcd(sum1,c)
print(sum2)
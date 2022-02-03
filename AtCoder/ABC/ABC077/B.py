import math
n=int(input())
sum=n
for i in range(1,n):
    if n >= i*i:
        sum = i*i
    else:
        break
print(sum)
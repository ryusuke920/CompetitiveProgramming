import math
n = int(input())
count = [0]*(10**7)
for i in range(1,101):
    for j in range(1,101):
        for k in range(1,101):
            count[i*i + j*j + k*k + i*j + j*k + k*i -1] += 1
for i in range(n):
    print(count[i])
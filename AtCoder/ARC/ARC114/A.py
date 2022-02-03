import math
from itertools import product
n = int(input())
x = list(map(int,input().split()))
num = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
ans = []

for i in product([0, 1], repeat = len(num)):
    cnt = 1
    for j in range(len(num)):
        if i[j] == 1: # 1 <-> bitが立っている時
            cnt *= num[j]
    check = True
    for j in range(n):
        if math.gcd(cnt, x[j]) == 1:
            check = False
    if check:
        ans.append(cnt)
print(min(ans))
#マンハッタン距離： |x1|+…+|xN|
#ユークリッド距離： √|x1|^2+…+|xN|^2
#チェビシェフ距離： max(|x1|,…,|xN|)

#in
#10
#3 -1 -4 1 -5 9 2 -6 5 -3

#out
#39
#14.387494569938159
#9
import math
n = int(input())
x = list(map(int,input().split()))
num = 0
for i in range(n):
    x[i] = abs(x[i])
    num += x[i]**2
print(sum(x))
print(math.sqrt(num))
print(max(x))
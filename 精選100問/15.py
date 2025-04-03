from itertools import permutations
import math
n = int(input())
d = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in permutations(range(n)):
    cnt  = 0
    for j in range(n-1):
        cnt += math.sqrt((d[i[j]][0] - d[i[j+1]][0])**2 + (d[i[j]][1] - d[i[j+1]][1])**2)
    ans += cnt
print(ans/math.factorial(n))
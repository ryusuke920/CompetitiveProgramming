from math import floor
n, K = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
ans = []
from collections import defaultdict
for i in range(n - K + 1):
    for j in range(n - K + 1):
        if j == 0:
            num = []
            ta = []
            for k in range(K):
                for l in range(K):
                    num.append(a[k + i][l + j])
                    ta.append(a[k + i][l + j])
            num.sort()
            ta = ta[2:]
            ans.append(num[K ** 2 - floor(K ** 2 / 2) - 1])
        else:
            #print("始まり",ta)
            for k in range(K):
                ta.append(a[i + k][j + K - 1])
            tb = ta
            ta.sort()
            tb = tb[2:]
            ans.append(ta[K ** 2 - floor(K ** 2 / 2) - 1])
        #print(i,j,ans)
print(min(ans))
#ans.sort()
#print(ans)
#print(ta)
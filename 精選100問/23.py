# 半分全列挙
from bisect import bisect_left
n,m = map(int,input().split())
a = [0]*n
for i in range(n):
    a[i] = int(input())
a.append(0)
num = []
for i in range(n):
    for j in range(i,n+1):
        num.append(a[i] + a[j])
num.sort()

ans = 0
for i in range(len(num)):
    if num[i] < m:
        ans = max(ans, num[i])
    x = m - num[i] 
    if x > 0: # 更に２本打っちゃうよーーー
        y = bisect_left(num, x)
        #print(i,y,x,ans)
        if y > 0 and num[i] + num[y-1] <= m: # 0だと追加する必要ないしバグるね
            ans = max(ans, num[i] + num[y-1])
print(ans)
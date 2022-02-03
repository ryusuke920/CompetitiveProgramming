n = int(input())
a = list(map(int,input().split()))

ans1 = 0
num1 = a[0]
# 初項が＋の場合
if a[0] <= 0:
    ans1 += abs(a[0]) + 1
    num1 = 1
for i in range(n - 1):
    if i%2 == 0: # +の時
    else: # -の時
import math
n,k = map(int,input().split())
a = list(map(int,input().split()))
ma = max(a)
mi = 0
while ma - mi > 1:
    mid = (ma + mi)//2
    s = 0
    for i in a:
        s += math.ceil(i/mid) - 1
    if s > k: # もっと大きくできる
        mi = mid
    else: # kがすべての和を超えているので、絞り込まなきゃいけない
        ma = mid
print(ma) # なんとなく+1したら全部合いそう（ACした。。。）
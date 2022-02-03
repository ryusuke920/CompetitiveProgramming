from collections import Counter
n,m = map(int,input().split())
a = list(map(int,input().split()))
x = Counter(a)
ch = n//2
if x.most_common()[0][1] > ch:
    print(x.most_common()[0][0])
else:
    print('?')
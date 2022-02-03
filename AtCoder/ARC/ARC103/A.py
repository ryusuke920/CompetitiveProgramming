n = int(input())
a = list(map(int,input().split()))
from collections import Counter
ki = a[1::2]
gu = a[0::2]
x = Counter(ki)
y = Counter(gu)
#print(x,y)
if x.most_common()[0][1] == y.most_common()[0][1] and x.most_common()[0][0] == y.most_common()[0][0]:
    if len(x) == 1 or len(y) == 1:
        ans = min(x.most_common()[0][1], y.most_common()[0][1])
    elif x.most_common()[1][1] <= y.most_common()[1][1]:
        ans = n//2 - x.most_common()[0][1] + n//2 - y.most_common()[1][1]
    else:
        ans = n//2 - x.most_common()[1][1] + n//2 - y.most_common()[0][1]
else:
    ans = n//2 - x.most_common()[0][1] + n//2 - y.most_common()[0][1]
print(ans)
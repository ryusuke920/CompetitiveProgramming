n = int(input())
a,b = map(int,input().split())
k = int(input())
p = list(map(int,input().split()))
p.append(a)
p.append(b)
from collections import Counter
count = Counter(p)
for i in range(len(count)):
    if count.most_common()[i][1] >= 2:
        print("NO")
        break
else:
    print("YES")
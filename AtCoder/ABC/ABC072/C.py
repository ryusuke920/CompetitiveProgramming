n = int(input())
a = list(map(int,input().split()))
ans = a
for i in range(n):
    ans.append(a[i]+1)
    ans.append(a[i]-1)
from collections import Counter
num = Counter(ans)
print(num.most_common()[0][1])
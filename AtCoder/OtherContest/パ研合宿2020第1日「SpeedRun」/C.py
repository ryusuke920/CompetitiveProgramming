n = int(input())
num = []
for i in range(n):
    k = int(input())
    s = list(map(str,input().split()))
    for j in range(k):
        num.append(s[j])
from collections import Counter
x = Counter(num)
x = x.most_common()
ans = 0
for i in range(len(x)):
    if x[i][1] == n:
        ans += 1
print(ans)
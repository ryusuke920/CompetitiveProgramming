n = int(input())
s = [input() for _ in range(n)]
from collections import Counter
ans = 10 ** 9
for i in range(n - 1):
    x = Counter(s[i])
    num = 0
    for j in range(i + 1 , n):
        y = Counter(s[j])
        z = (x - y) + (y - x)
        num = 0
        for k in range(len(z)):
            num += z.most_common()[k][1]
        #print(s[i],s[j],num,z,len(s[i]),len(s[j]),z.most_common()[k][1])
        if num / min(len(s[i]), len(s[j])) < ans:
            ans1 = s[i]
            ans2 = s[j]
            ans = num / min(len(s[i]), len(s[j]))
print(ans1)
print(ans2)
t = str(ans)
if len(t) >= 5:
    print(str(ans)[:5])
else:
    ans = str(ans)
    for i in range(5 - len(ans)):
        ans += '0'
    print(str(ans)[:5])
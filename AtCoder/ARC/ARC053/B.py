from collections import Counter
from math import floor
s = list(input())
num = Counter(s).most_common()
odd, even = [], []
for i in range(len(num)):
    if num[i][1] % 2 == 0:
        odd.append(num[i][1])
    else:
        even.append(num[i][1])
even.sort() # 奇数
odd.sort() # 偶数

if len(even) == 0:
    print(len(s))
else:
    k = len(even)
    print(1 + 2 * floor((len(s) - k) / (2 * k)) )
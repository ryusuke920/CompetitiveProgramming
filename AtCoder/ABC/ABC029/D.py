from bisect import bisect_left
from collections import deque
n = int(input())
ans = 0
num = deque()
num.append(1)
ans = 0
for i in range(1, len(str(n))):
    ans += n % 10 ** i
print(ans)
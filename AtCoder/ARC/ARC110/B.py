n = int(input())
ch = "110"*(n+1)
t = input()
cnt = ans = 0
a1 = 0
d = 0
i = 0
if n == 1 and t == "1":
    exit(print(2*10**10))
elif n == 1 and t == "0":
    exit(print(10**10))
while True:
    if i == 10:
        exit(print(0))
    if ch[i:i+n] == t:
        if cnt == 0:
            a1 = i + n
        cnt += 1
    if cnt == 2:
        d = i + n - a1
        break
    i += 1

import math
ans = math.floor((3*10**10 - a1 + d)/d)
print(ans)
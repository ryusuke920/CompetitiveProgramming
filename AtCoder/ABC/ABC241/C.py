from itertools import product
from collections import deque

n = int(input())
s = [input() for _ in range(n)]

ans = set()
for i in product([0, 1], repeat=6):
    cnt = i.count(0)
    num = ''
    if cnt < 3:
        for j in range(6):
            if i[j] == 1:
                num += '#'
            else:
                num += '.'
        ans.add(num)

num = set()
for i in s: num.add(i)

tmp = ''
for i in range(n ** 2):
    cnt = i % n
    if cnt != n - 1:
        tmp += s[i % n][i // n]
    else:
        tmp += s[i % n][i // n]
        num.add(tmp)
        tmp = ''

c_1 = ['' for _ in range(2 * n - 1)]
c_2 = ['' for _ in range(2 * n - 1)]

for i in range(n):
    for j in range(n):
        c_1[i - j] += s[i][j]
        c_2[i - j] += s[i][n - j - 1]

for i in c_1: num.add(i)
for i in c_2: num.add(i)

for i in num:
    for j in ans:
        if j in i:
            exit(print('Yes'))

print('No')
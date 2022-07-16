import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))

if n == 1:
    print('Yes')
    print(0, 0, s[0])
    exit()

ma_1, ma_2 = -1, -1
for i in range(n - 1):
    ma_1 = max(ma_1, s[i + 1] - s[i])
    ma_2 = max(ma_2, s[i] - s[i + 1])

a = [-1] * (n + 2)
for i in range(n - 1):
    if s[i + 1] - s[i] == ma_1:
        a[i + 3] = ma_1
    if s[i] - s[i + 1] == ma_2:
        a[i] = ma_2

for i in reversed(range(n + 2)):
    ind  = i
    if a[ind - 3] == -1:
        ind -= 3
        while ind >= 0:
            a[ind] = a[ind + 3] - (s[ind + 1] - s[ind])
            ind -= 3

if a[0] == -1 or a[1] == -1:
    print('No')
else:
    for i in range(2, n + 2):
        if a[i] == -1:
            a[i] = s[i - 2] - (a[i - 1] + a[i - 2])
    
    for i in range(n + 2):
        if a[i] < 0:
            exit(print('No'))
    
    print('Yes')
    print(*a)
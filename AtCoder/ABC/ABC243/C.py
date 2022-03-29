from collections import defaultdict

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
s = input()

d_left = defaultdict(lambda : -10 ** 18)
d_right = defaultdict(lambda : 10 ** 18)

for i in range(n):
    x, y = xy[i]
    if s[i] == 'L':
        d_left[y] = max(d_left[y], x)
    elif s[i] == 'R':
        d_right[y] = min(d_right[y], x)

for i in range(n):
    x, y = xy[i]
    if d_left[y] > d_right[y]:
        exit(print('Yes'))

print('No')
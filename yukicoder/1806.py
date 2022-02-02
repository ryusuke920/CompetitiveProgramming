from collections import defaultdict

a = input()
b = input()

d = defaultdict(int)
for i, j in enumerate('NESW'):
    d[j] = i

print((4 + d[b] - d[a]) % 4)
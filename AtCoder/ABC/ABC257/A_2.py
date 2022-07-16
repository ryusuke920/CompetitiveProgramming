n, x = map(int, input().split())

s = ''
for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    s += i * n


print(s[x - 1])
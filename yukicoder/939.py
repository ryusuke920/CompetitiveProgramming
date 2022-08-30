a, b = map(int, input().split())

if a == b:
    exit(print(1))

a = bin(a)[2:]
b = bin(b)[2:]

la, lb = len(a), len(b)
ma = max(la, lb)
if la != ma:
    a = '0' * (ma - la) + a
if lb != ma:
    b = '0' * (ma - lb) + b

num = 0
for i, j in zip(a, b):
    if (i, j) == ('1', '0'):
        exit(print(0))
    if i != j:
        num += 1

print(2 ** (num - 1))
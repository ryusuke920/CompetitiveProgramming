from collections import defaultdict

s = input()
d = defaultdict(int)
for i in s:
    d[i] += 1

bool = True
b = False
for i in s:
    if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        b = True
if not b:
    bool = False
b = False
for i in s:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        b = True
if not b:
    bool = False
for k, v in d.items():
    if v >= 2:
        bool = False

if bool:
    print('Yes')
else:
    print('No')
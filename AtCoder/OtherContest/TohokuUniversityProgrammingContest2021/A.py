from collections import defaultdict

m = int(input())
s1, s2 = input().split()

x, y = set(), set()
for i in s1:
    x.add(i)
for i in s2:
    y.add(i)

d = defaultdict(int)

for i in range(m):
    t1, t2 = input().split()
    a, b = set(), set()
    for j in t1:
        a.add(j)
    for j in t2:
        b.add(j)

    bool = True
    for ss in range(26):
        for tt in range(26):
            if chr(ss + 97) in x and chr(tt + 97) in y:
                if (chr(ss + 97) not in a) or (chr(tt + 97) not in b):
                    d[f'{chr(97 + int(ss))}_{chr(97 + int(tt))}'] += 1

ans = []
for k, v in d.items():
    aa, bb = k.split('_')
    if v == m:
        ans.append(aa + bb)

ans = sorted(list(set(ans)))

if len(ans):
    print('Yes')
    print(ans[0])
else:
    print('No')
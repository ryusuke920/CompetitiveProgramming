n = int(input())
a = [int("1" * i) for i in range(1, 20)]
l = len(a)
p = set()
for i in range(l):
    for j in range(l):
        for k in range(l):
            p.add(a[i] + a[j] + a[k])
p = list(p)
p.sort()
print(p[n - 1])
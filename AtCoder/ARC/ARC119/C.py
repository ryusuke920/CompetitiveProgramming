import copy
n = int(input())
a = list(map(int,input().split()))
ans = cnt = 0
b = copy.copy(a)
c = copy.copy(a)
c = c[::-1]
for i in range(n - 1):
    b[i + 1] += b[i]
    c[i + 1] += c[i]
d = [a[0]]
for i in range(n - 1):
    d.append(a[i + 1] - a[i] + d[i])
print(d)
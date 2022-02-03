n = int(input())
a = list(map(int,input().split()))
a.sort()
print(a)
t = 0
for i in range(n-  1):
    t+= a[i + 1] * (i + 1)
print(t)
wa = [0] * n
wa[0] = sum(a)
for i in range(n - 1):
    wa[i + 1] = wa[i] - a[i]
print(wa)
for i in range(n-1):
    t -= wa[i + 1]
    print(t)
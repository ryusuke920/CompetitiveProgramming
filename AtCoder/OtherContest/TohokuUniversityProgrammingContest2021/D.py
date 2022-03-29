n = int(input())
a = list(map(int, input().split()))

for i in range(n - 1):
    b = []
    diff = -10 ** 18
    for j in range(n - 1 - i):
        diff = max(diff, abs(a[j] - a[j + 1]))
    
    for j in range(n - 1 - i):
        if abs(a[j] - a[j + 1]) == diff:
            ind = j
            break
    
    for j in range(n - i):
        if j == ind: continue
        if j == ind + 1:
            b.append(diff)
        else:
            b.append(a[i])
    
    a = []
    for j in b:
        a.append(j)
    print(i, a)

print(a[0])
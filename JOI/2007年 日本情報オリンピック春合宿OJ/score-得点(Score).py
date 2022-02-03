n = int(input())
num = {}
for i in range(n):
    x = int(input())
    if x not in num:
        num[x] = [i]
    else:
        num[x].append(i)

rank = [0] * n
t = 1
for i, j in enumerate(sorted(num.keys(), reverse = True)):
    for k in num[j]:
        rank[k] = t
    t += len(num[j])
print(*rank, sep = "\n")
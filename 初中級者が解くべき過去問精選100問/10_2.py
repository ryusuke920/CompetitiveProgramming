from itertools import product
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
ans = []
for i in list(product([0,1], repeat = n)):
    num = 0
    for j in range(n):
        if i[j] == 1:
            num += a[j]
    ans.append(num)
ans = set(ans)
for i in range(m):
    if b[i] in ans:
        print("yes")
    else:
        print("no")
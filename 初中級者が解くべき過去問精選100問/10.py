n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
num = []
for i in range(2**n):
    ans = 0
    for j in range(n):
        if (i>>j) & 1:
            ans += a[j]
    num.append(ans)

for i in range(m):
    if b[i] in set(num):
        print("yes")
    else:
        print("no")
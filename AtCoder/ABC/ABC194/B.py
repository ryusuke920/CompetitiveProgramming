n = int(input())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int,input().split())
ans = 10 ** 18
for i in range(n):
    ans = min(ans ,a[i] + b[i])
x = y = 10 ** 18

for i in range(n):
    for j in range(n):
        if i == j: continue
        #print(i,j,a[i] + b[j])
        x = min(x,max(a[i], b[j]))
print(min(ans,x))
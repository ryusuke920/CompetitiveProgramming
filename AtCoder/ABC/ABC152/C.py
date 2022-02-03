n = int(input())
p = list(map(int,input().split()))
count = 0
mi = n+1
for i in range(n):
    mi = min(mi,p[i])
    if mi == p[i]:
        count += 1
print(count)
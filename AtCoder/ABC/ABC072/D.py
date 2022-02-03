n = int(input())
p = list(map(int,input().split()))
count = 0
for i in range(n-1):
    if p[i] == i+1:
        tmp = p[i]
        p[i] = p[i+1]
        p[i+1] = tmp
        count += 1
if p[-1] == n:
    count += 1
print(count)
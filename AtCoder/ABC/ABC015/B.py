n = int(input())
a = list(map(int,input().split()))
ans = 0
count = 0
for i in range(n):
    ans += a[i]
    if a[i] == 0:
        count += 1
if ans%(n-count) == 0:
    print((ans)//(n-count))
else:
    print(ans//(n-count)+1)
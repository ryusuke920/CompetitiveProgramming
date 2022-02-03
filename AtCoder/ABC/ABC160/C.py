k,n = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
ch = 0
for i in range(n-1):
    if a[i+1] - a[i] >= ch:
        ch = a[i+1] - a[i]
ch = max(ch, k -a[n-1] + a[0])
print(k-ch)
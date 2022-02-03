n,t = map(int,input().split())
a = [int(input()) for i in range(n)]
count = 0
for i in range(n-1):
    if a[i+1] - a[i] < t:
        count += a[i+1] - a[i]
    else:
        count += t
print(count+t)
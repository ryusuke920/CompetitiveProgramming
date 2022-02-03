n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
cnt = 0
for i in range(n):
    cnt += min(a[i],b[i])
    if b[i] > a[i]:
        if a[i+1] >= b[i] - a[i]:
            cnt += b[i] - a[i]
            a[i+1] -= b[i] - a[i]
        else:
            cnt += a[i+1]
            a[i+1] = 0
print(cnt)
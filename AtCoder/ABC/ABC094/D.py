n = int(input())
a = list(map(int,input().split()))
ma = max(a)
cnt = 10**9
mid = ma/2
for i in range(n):
    if abs(cnt - mid) >= abs(mid - a[i]):
        cnt = a[i]
print(max(ma,cnt),min(ma,cnt))
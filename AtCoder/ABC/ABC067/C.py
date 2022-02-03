n = int(input())
a = list(map(int,input().split()))
front = 0
rear = sum(a)
ans = 10**100
for i in range(n-1):
    front += a[i]
    rear -= a[i]
    ans = min(ans,abs(front - rear))
print(ans)
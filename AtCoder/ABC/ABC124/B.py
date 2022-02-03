n = int(input())
h = list(map(int,input().split()))
count = 1
ans = h[0]
for i in range(1,n):
        if h[i] >= ans:
            count += 1
        ans = max(ans,h[i])
print(count)
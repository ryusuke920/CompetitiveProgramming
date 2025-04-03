n = int(input())
ab = [tuple(map(int,input().split())) for _ in range(n)]
abset = set(ab)
ans = 0
for i in range(n-1):
    for j in range(i+1,n):
        x1, y1 = ab[i]
        x2, y2 = ab[j]
        dx = x2-x1
        dy = y2-y1
        if ((x1+dy, y1-dx) in abset) and ((x2+dy, y2-dx) in abset):
            ans = max(ans, dx**2+dy**2)
print(ans)
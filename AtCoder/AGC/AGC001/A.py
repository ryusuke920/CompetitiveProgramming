n = int(input())
l = list(map(int,input().split()))
ans = 0
l.sort()
for i in range(n):
    ans += l[0]
    l = l[2:]
print(ans)
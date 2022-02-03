n = int(input())
p = [int(input()) for i in range(n)]
p.sort()
ans = 0
for i in range(n-1):
    ans += p[i]
print(ans + p[-1]//2)
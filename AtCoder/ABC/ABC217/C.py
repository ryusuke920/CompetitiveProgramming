n = int(input())
p = list(map(int,input().split()))
ans = [0] * n
for i, j in enumerate(p):
    ans[j - 1] = i + 1

print(*ans)
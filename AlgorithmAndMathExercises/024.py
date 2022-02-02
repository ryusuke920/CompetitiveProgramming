n = int(input())

ans = 0
for _ in range(n):
    p, q = map(int, input().split())
    ans += q / p

print(ans)
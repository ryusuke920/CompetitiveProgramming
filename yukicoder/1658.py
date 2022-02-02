n, k = map(int, input().split())

ans = [2 * k, n - 2 + 2 * k]
for _ in range(n - 2):
    ans.append(1)

print(*ans)
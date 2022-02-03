n = int(input())
k = int(input())
s = [input() for _ in range(n)]
d = ((0, 1), (0, -1), (1, 0), (-1, 0))

memo = set()
def dfs(ps):
    if tuple(sorted(ps)) in memo: return 0
    memo.add(tuple(sorted(ps)))
    if len(ps) == k: return 1
    ans = 0
    for x, y in ps:
        for dx, dy in d:
            if not (0 <= x + dx <= n - 1 and 0 <= y + dy <= n - 1): continue
            if s[y + dy][x + dx] == "." and (y + dy, x + dx) not in ps:
                ans += dfs(ps + [(y + dy, x + dx)])
    return ans

ans = 0
for i in range(n):
    for j in range(n):
        if s[i][j] == ".":
            ans += dfs([(i, j)])
print(ans)
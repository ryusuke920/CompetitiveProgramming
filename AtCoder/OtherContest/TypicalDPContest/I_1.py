s = input()

# dp[i] := i文字目まででできる操作の最大値
# is_ok[l][r] := [l, r)で行うことのできる操作の最大値
# is_ok[l][r] := [l, r)までを全て取り切ることができるかどうか（上記のができれば必然的に達成できる）

n = len(s)
dp = [0] * (n + 1)
is_ok = [[False] * (n + 1) for _ in range(n)]

for i in range(n):
    for j in range(n + 1):
        if i >= j:
            is_ok[i][j] = True

for w in range(n + 1):
    for l in range(n + 1):
        r = l + w
        if r > n:
            continue
        for mid in range(l, r):
            # [iwi], [iwi] を引っ付けるパターン
            is_ok[l][r] |= (is_ok[l][mid] and is_ok[mid][r])
            # i, [iwi], w, [iwi], i を引っ付けるパターン (w := mid とする)
            if s[l] == "i" and s[mid] == "w" and s[r - 1] == "i":
                is_ok[l][r] |= (is_ok[l + 1][mid] and is_ok[mid + 1][r - 1])

for r in range(n + 1):
    if r >= 1:
        dp[r] = max(dp[r], dp[r - 1])
    for l in range(r):
        if is_ok[l][r]:
            dp[r] = max(dp[r], dp[l] + (r - l) // 3)

# print(*is_ok, sep="\n")
# print(dp)
print(dp[n])
n, r = map(int,input().split())
s = list(input())[::-1]
ans = tmp = 0
for i in range(n):
    if s[i] == ".": # 塗るべき場所
        if tmp == 0:
            tmp = max(0, n - r - i)

        ans += 1 # 塗る回数

        # 銃で攻撃
        for j in range(r):
            if i + j <= n - 1:
                s[i + j] = "o"

print(ans + tmp)
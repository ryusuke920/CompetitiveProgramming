n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())

# 初期状態は全て . にする
ans = [["."] * (s - r + 1) for _ in range(q - p + 1)]

# １つ目の条件について探索する
for i in range(p, q + 1):
    for j in range(r, s + 1):
        dx = i - a # x座標の増加量
        dy = j - b # y座標の増加量
        if dx == dy: # x座標の増加量 = y座標の増加量 の場合に条件を満たす
            if max(1 - a, 1 - b) <= dx <= min(n - a, n - b):
                ans[i - p][j - r] = "#" # -p, -r は (p, r)スタートのために並行移動する

# ２つ目の条件について探索する
for i in range(p, q + 1):
    for j in range(r, s + 1):
        dx = i - a # x座標の増加量
        dy = j - b # y座標の増加量
        if dx == -dy: # x座標の増加量 = -y座標の増加量 の場合に条件を満たす
            if max(1 - a, b - n) <= dx <= min(n - a, b - 1):
                ans[i - p][j - r] = "#" # -p, -r は (p, r)スタートのために並行移動する

for i in ans:
    print(*i, sep="")
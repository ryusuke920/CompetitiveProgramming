n = int(input())
s = [list(input()) for _ in range(n)]
t = [list(input()) for _ in range(n)]

ch = [["0"]*n for _ in range(n)] # 調べ上げる配列を生成
num1 = num2 = 1
num3 = 2
num4 = 0

# 1. 時計回り
for i in range(n):
    for j in range(n):
        ch[i][j] = s[n - j - 1][i] # 時計回りした配列を作成

# そこから数え上げ
for i in range(n):
    for j in range(n):
        if ch[i][j] != t[i][j]:
            num1 += 1

# 2. 反時計回り
for i in range(n):
    for j in range(n):
        ch[i][j] = s[j][n - i - 1] # 時計回りした配列を作成

# そこから数え上げ
for i in range(n):
    for j in range(n):
        if ch[i][j] != t[i][j]:
            num2 += 1

# 3. 90°回転
for i in range(n):
    for j in range(n):
        ch[i][j] = s[n - i - 1][n - j - 1] # 時計回りした配列を作成

# そこから数え上げ
for i in range(n):
    for j in range(n):
        if ch[i][j] != t[i][j]:
            num3 += 1

# 4. 全探索
for i in range(n):
    for j in range(n):
        if s[i][j] != t[i][j]:
            num4 += 1

print(min(num1, num2, num3, num4))
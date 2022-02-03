n = int(input())

cnt = [[0] * 10 for _ in range(10)] # cnt[i][j] := 先頭がiで末尾がjである数
for i in range(1, n + 1):
    btm = i % 10 # 末尾
    top = int(str(i)[0]) # 先頭
    cnt[top][btm] += 1

ans = 0
for i in range(10):
    for j in range(10):
        ans += cnt[i][j] * cnt[j][i]
print(ans)
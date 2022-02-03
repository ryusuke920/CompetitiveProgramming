s = str(input())
cnt = 0
ans = "CODEFESTIVAL2016"
for i in range(16):
    if s[i] != ans[i]:
        cnt += 1
print(cnt)
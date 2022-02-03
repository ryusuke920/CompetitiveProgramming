s = input()
check = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = []
i = 0
while True:
    if s[i] in check:
        word = ""
        word += s[i]
        cnt = i + 1
        while True:
            if s[cnt] not in check:
                word += s[cnt]
            else:
                word += s[cnt]
                ans.append([word.upper(), word])
                break
            cnt += 1
    else:
        i += 1
    i = cnt + 1
    if i >= len(s) - 1:
        break
ans.sort()

words = []
for i in range(len(ans)):
    words.append(ans[i][1])
print(*words, sep = "")
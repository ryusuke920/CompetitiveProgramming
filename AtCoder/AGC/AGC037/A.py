s = str(input())
cnt = 1
ans = s[0]
word = ""
for i in range(1,len(s)):
    word += s[i]
    if word != ans:
        cnt += 1
        ans = word
        word = ""
print(cnt)
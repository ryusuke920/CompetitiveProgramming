s = list(input())
ans = 0
ch = 0
num = 0
word = "ryusuke"
p = 10 ** 18
for i in range(len(s) - 2):
    if ch == 1 and word == s[i] and i - p != 1:
        num += 1
    if s[i + 1] == s[i] and s[i + 1] != s[i + 2] and s[i + 2] != s[i]:
        if s[i] != word:
            word = s[i + 1]
            p = i
            ans += max(len(s) - i - 2, 0)
            ch = 1
        else:
            num += 1

print(ans - num)
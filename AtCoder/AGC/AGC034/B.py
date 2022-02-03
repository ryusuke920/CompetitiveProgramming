S = input()
s = ""
if len(S) == 1:
    s = S
else:
    i = 0
    while i <= len(S) - 1:
        if i != len(S) - 1:
            if S[i] + S[i + 1] == "BC":
                s += "D"
                i += 1
            else:
                s += S[i]
        else:
            s += S[i]
        i += 1

# Aから始まって以降 A or D になってる部分文字列を words に打ち込む
i = 0
ch = 0
word = ""
words = []
while i <= len(s) - 1:
    if s[i] == "A" and len(word) == 0:
        word += "A"
    elif len(word) >= 1 and (s[i] == "D" or s[i] == "A"):
        word += s[i]
    else:
        if len(word) >= 2:
            words.append(word)
        word = ""
        if s[i] == "A":
            word += "A"
    i += 1
if len(word) >= 2:
    words.append(word)

ans = 0
for i in range(len(words)):
    cnt_d = 0 # Dが何個目まであるかを判別するやつ
    for j in range(len(words[i])):
        if j == 0: continue # 最初はA
        if words[i][j] == "D":
            ans += j - cnt_d # D が左に詰まっていくから引いていくイメージ
            cnt_d += 1
print(ans)